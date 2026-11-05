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



def top_artists(music,n=10):

    artists = {}

    # Create a dictionary of artists and the amount of times they have been listened to
    for play in music:
        artist = play['master_metadata_album_artist_name']

        # Rather than the if/else statement, now .get() returns the value of the artists count in the artists dic, if not there, it sets the default value to 0
        artists[artist] = artists.get(artist, 0) + 1

    # To get key value pairs you need to use .items() to turn them into tuples, iterating directly over a dic only gives you the keys
    sorted_artists = dict(sorted(artists.items(), key=lambda x: x[1], reverse=True))
    
    # Create a list of the first 10 artist key value pairs and turn that into a dictionary, as if you want key value pairs, you need the tuples
    return dict(list(sorted_artists.items())[:n])

    


history = load_history(folder)
music = music_only(history)
total_hrs = total_hours(history)
n = 10
top_10 = top_artists(music,n)
print(top_10)
