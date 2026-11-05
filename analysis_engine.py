from pathlib import Path
import json
from collections import Counter

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

    # Counter iterates over an iterable and creates a dictionary where each key is an item from the iterable and its value is the number of times that item has been seen. 
    return Counter(play['master_metadata_album_artist_name'] 
                   for play in music).most_common(n)





def top_tracks(music,n=10):

    # List comprehension - add the tuple into the list song for each play
    songs = [(play['master_metadata_track_name'], 
              play['master_metadata_album_artist_name']) for play in music]

    # Use Counter() to create the dicitonary for {song:count}, then most_common(n) returns a list of (song, count) pairs of the n most common
    return Counter(songs).most_common(n)






history = load_history(folder)
music = music_only(history)
total_hrs = total_hours(music)
n = 10
top_n_artists = top_artists(music)
top_n_tracks = top_tracks(music)
print(top_n_tracks)
