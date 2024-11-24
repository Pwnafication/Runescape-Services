from flask import Flask, render_template, redirect, url_for, json
from random import randint
import os
import webbrowser
from threading import Timer

# Initialize Flask
app = Flask(__name__)

# Define the Pokémon data and class
poke_data = {
    "pikachu": {"hp": 500, "atk": 10},
    "charmander": {"hp": 500, "atk": 10},
    "squirtle": {"hp": 500, "atk": 10},
    "bulbasaur": {"hp": 500, "atk": 10}
}

class pokeObject:
    def __init__(self, name, hp, atk, gift=0):
        self.name = name.title()
        self.hp = hp
        self.atk = atk
        self.gift = gift


# Load win counts from JSON
def load_wins():
    if not os.path.exists('wins.json'):
        return {name: 0 for name in poke_data}  # Initialize win count for all Pokémon
    with open('wins.json', 'r') as f:
        return json.load(f)


# Save win counts to JSON
def save_wins(wins):
    with open('wins.json', 'w') as f:
        json.dump(wins, f)


# Initialize Pokémon objects
poke_list = [pokeObject(name, poke_data[name]['hp'], poke_data[name]['atk']) for name in poke_data]


# Battle logic
def battle():
    poke_list_copy = poke_list[:]  # Create a copy of the list for each battle
    go = True
    while go and len(poke_list_copy) > 1:
        poke1 = poke_list_copy[randint(0, len(poke_list_copy)-1)]
        poke2 = poke_list_copy[randint(0, len(poke_list_copy)-1)]
        
        # Ensure poke1 and poke2 are different
        while poke1 == poke2:
            poke2 = poke_list_copy[randint(0, len(poke_list_copy)-1)]
        
        # Simulate gift giving
        gifts = randint(0, 3) * poke1.atk
        poke2.gift += gifts
        if poke2.gift > 9999:
            go = False  # End battle when one Pokémon "faints"
            poke_list_copy.remove(poke2)
    
    return poke_list_copy[0]  # Return the winner


#flask routes
@app.route('/')
def index():
    return render_template('index.html', poke_list=poke_list)

@app.route('/battle', methods=['POST'])
def start_battle():
    winner=battle()
    wins=load_wins()

