import json


def get_titles_lyrics():
    # Load the JSON file.
    with open('src/Lyrics_TaylorSwift.json') as f:
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
