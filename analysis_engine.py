from pathlib import Path
import json


folder = Path('my_spotify_data/Spotify Extended Streaming History')


def load_history(folder):

    history = []

    for file_path in sorted(folder.glob('*Audio*.json')):
        with open(file_path) as f:
            history.extend(json.load(f))

    return history 

        

def total_hours(history):

    total_ms = sum(play['ms_played'] for play in history)

    total_hrs = round(total_ms / (1000*3600),2)
 
    return total_hrs





history = load_history(folder)
total_hrs = total_hours(history)
print(total_hrs)
