import json
import os

def get_titles_lyrics():
    # Get the directory of this script.
    dir_path = os.path.dirname(os.path.realpath(__file__))
    # Construct the full path to the JSON file.
    json_path = os.path.join(dir_path, 'Lyrics_TaylorSwift.json')
    with open(json_path) as f:
    # Load the JSON file.
        data = json.load(f)
    # Access 'songs' key which is a list of dictionaries.
    songs = data['songs']
    song_details = []
    # Iterate over the json file and access 'lyrics' and 'title_with_featured' keys for each song.
    for song in songs:
        if 'lyrics' in song and 'title_with_featured' in song:
            lyrics = song['lyrics']
            title_with_featured = song['title_with_featured']
            song_details.append((title_with_featured, lyrics))
    return song_details