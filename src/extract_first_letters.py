
from text_formatting import text_formatting
from reading_jsonfile import get_titles_lyrics


def extract_title_first_letters(song_details):
    # Initialize an empty list to store song titles details with their full name and the first each letter of each words. This will not be done is the title song is only two word.
    title_details = []
    # Loop through each song's titles.
    for song in song_details:
        # Access the title
        title = song[0]
        title, words = text_formatting(title)
        # Get the first letter of each word if only there are more than two words.
        first_letters = [word[0] for word in words] if len(words) > 2 else []
        # Add the full title and corresponding first letters to individual list in title_details.
        title_details.append([title, first_letters])
    return title_details


def extract_lyric_first_letters(song_details):
    # Initalised an empty list to store lyrics details and first letter of lyrics' words.
    lyrics_details = []
    # Loop through each song's lyrics.
    for song in song_details:
        # Access the lyrics.
        lyrics = song[1]
        lyrics, words = text_formatting(lyrics)
        # Returning only the first letter of each words in the lyric.
        first_letters_lyrics = [[word[0]] for word in words]
        # Putting each song's lyrics and their corresponding first letter in its own list.
        lyrics_details.append([lyrics,first_letters_lyrics])
    return lyrics_details


song_details = get_titles_lyrics()
title_details = extract_title_first_letters(song_details)
lyrics_details = extract_lyric_first_letters(song_details)