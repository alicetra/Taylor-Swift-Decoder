def get_titles_lyrics(data):
    # Access 'songs' key which is a list of dictionaries
    songs = data['songs']
    # # Initialize a counter to check it is reading all songs lyrics and titles
    # count = 0
    # Initialize an empty list to store song details
    song_details = []
    # Iterate over the json file and access 'lyrics' and 'title_with_featured' keys for each song
    for song in songs:
        if 'lyrics' in song and 'title_with_featured' in song:
            lyrics = song['lyrics']
            title_with_featured = song['title_with_featured']
            song_details.append((title_with_featured, lyrics))
            # count += 1
    return song_details