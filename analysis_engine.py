from pathlib import Path
import json


folder = Path('my_spotify_data/Spotify Extended Streaming History')


def load_history(folder):

    history = []

    for x in folder.glob('*Audio*.json'):
        with open(x) as f:
            history.extend(json.load(f))

    return history 

        
history = load_history(folder)
print(len(history))