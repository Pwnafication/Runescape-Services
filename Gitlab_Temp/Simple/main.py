from flask import Flask, render_template, redirect, url_for, json
import os
import webbrowser
from threading import Timer

app = Flask(__name__)

# Get the directory where the main.py file is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Function to load the click count from a JSON file
def load_clicks():
    json_path = os.path.join(BASE_DIR, 'clicks.json')  # Ensure clicks.json is in the same directory as main.py
    if not os.path.exists(json_path):
        return {'count': 0}
    with open(json_path, 'r') as f:
        return json.load(f)

# Function to save the click count to a JSON file
def save_clicks(clicks):
    json_path = os.path.join(BASE_DIR, 'clicks.json')  # Ensure clicks.json is in the same directory as main.py
    with open(json_path, 'w') as f:
        json.dump(clicks, f)

# Route 1: Index page
@app.route('/')
def index():
    return render_template('index.html')

# Route 2: Loot page (increments count)
@app.route('/loot', methods=['GET', 'POST'])
def loot():
    clicks = load_clicks()
    clicks['count'] += 1
    save_clicks(clicks)
    return render_template('loot.html', count=clicks['count'])

# Route 3: Homebase page (shows total count)
@app.route('/homebase')
def homebase():
    clicks = load_clicks()
    return render_template('homebase.html', count=clicks['count'])

# Open browser to the index page
def open_browser():
    webbrowser.open_new("http://127.0.0.1:5000/")

# Run the app and automatically open the browser
if __name__ == '__main__':
    # Only open the browser if this is the main process and not the reloader
    if os.environ.get('WERKZEUG_RUN_MAIN') == 'true':
        Timer(1, open_browser).start()

    app.run(debug=True)
