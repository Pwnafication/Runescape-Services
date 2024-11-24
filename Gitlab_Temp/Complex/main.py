from flask import Flask, render_template, redirect, url_for, json, jsonify
import os
import time
import webbrowser
from threading import Timer

app = Flask(__name__)

MAX_ENERGY = 100  # Maximum energy limit
ENERGY_REGEN_RATE = 1  # 1 energy per second


class EnergySystem:
    def __init__(self):
        self.energy = MAX_ENERGY
        self.gold = 0  # Initialize gold accumulation
        self.timestamps = []  # Store last 10 timestamps
        self.last_energy_update = time.time()  # Store last time energy was updated (Unix time)

    def load_state(self):
        """Load energy, gold, and timestamps from JSON."""
        if os.path.exists('energy.json'):
            with open('energy.json', 'r') as f:
                data = json.load(f)
                self.energy = data.get('energy', MAX_ENERGY)
                self.gold = data.get('gold', 0)  # Load gold, default to 0 if not found
                self.timestamps = data.get('timestamps', [])
                self.last_energy_update = data.get('last_energy_update', time.time())

    def save_state(self):
        """Save energy, gold, and timestamps to JSON."""
        with open('energy.json', 'w') as f:
            json.dump({
                'energy': self.energy,
                'gold': self.gold,  # Save gold
                'timestamps': self.timestamps,
                'last_energy_update': self.last_energy_update
            }, f)

    def update_energy(self):
        """Update energy based on how much time has passed."""
        current_time = time.time()
        time_diff = current_time - self.last_energy_update
        # Regenerate energy based on time difference
        energy_regen = int(time_diff * ENERGY_REGEN_RATE)
        self.energy = min(self.energy + energy_regen, MAX_ENERGY)  # Cap at max energy
        self.last_energy_update = current_time
        self.save_state()

    def add_timestamp(self):
        """Add a new timestamp for tracking the last 10 actions."""
        self.timestamps.append(time.time())
        if len(self.timestamps) > 10:
            self.timestamps.pop(0)  # Keep only the last 10 timestamps
        self.save_state()

    def use_energy_and_earn_gold(self):
        """Consume energy and accumulate Gold when a click is made."""
        if self.energy > 0:
            self.energy -= 1
            self.gold += 1  # Earn 1 Gold for each action
            self.add_timestamp()
            self.save_state()
            return True
        return False


# Initialize the energy system
energy_system = EnergySystem()
energy_system.load_state()


# Route 1: Index page (update energy and timestamps)
@app.route('/')
def index():
    energy_system.update_energy()
    energy_system.add_timestamp()
    return render_template('index.html', energy=energy_system.energy, gold=energy_system.gold)


# Route 2: Loot page (update energy, earn gold, and timestamps)
@app.route('/loot', methods=['GET'])
def loot():
    energy_system.update_energy()
    energy_system.add_timestamp()
    return render_template('loot.html', energy=energy_system.energy, gold=energy_system.gold)


# API Route: Increment click count (used for AJAX calls)
@app.route('/api/increment_clicks', methods=['POST'])
def increment_clicks():
    energy_system.update_energy()
    if energy_system.use_energy_and_earn_gold():
        return jsonify({'energy': energy_system.energy, 'gold': energy_system.gold})
    else:
        return jsonify({'error': 'Not enough energy!'}), 400


# Route 3: Homebase page (update energy and timestamps)
@app.route('/homebase')
def homebase():
    energy_system.update_energy()
    energy_system.add_timestamp()
    return render_template('homebase.html', energy=energy_system.energy, gold=energy_system.gold, timestamps=energy_system.timestamps)


def open_browser():
    webbrowser.open_new("http://127.0.0.1:5000/")


if __name__ == '__main__':
    if os.environ.get('WERKZEUG_RUN_MAIN') == 'true':
        Timer(1, open_browser).start()
    app.run(debug=True)
