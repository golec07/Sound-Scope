from pathlib import Path
import json


folder = Path('my_spotify_data/Spotify Extended Streaming History')


def load_history(folder):

    history = []

    for file_path in sorted(folder.glob('*Audio*.json')):
        with open(file_path) as f:
            history.extend(json.load(f))

    return history 



def music_only(history):

    return [play for play in history if play['master_metadata_track_name'] is not None]




def total_hours(music):

    total_ms = sum(play['ms_played'] for play in history)

    total_hrs = round(total_ms / (1000*3600),2)
 
    return total_hrs





history = load_history(folder)
music = music_only(history)
total_hrs = total_hours(history)
print(len(history)-len(music))
