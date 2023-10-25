
from text_formatting import text_formatting
from reading_jsonfile import get_titles_lyrics


def extract_title_first_letters(song_details):
    # Initialize an empty list to store song titles details with their full name and the first each letter of each words. This will not be done is the title song is only two word
    title_details = []
    # Loop through each song's titles
    for song in song_details:
        # Access the title
        title = song[0]
        title, words = text_formatting(title)
        # Get the first letter of each word if only there are more than two words
        first_letters = [word[0] for word in words] if len(words) > 2 else []
        # Add the full title and corresponding first letters to individual list in title_details
        title_details.append([title, first_letters])
    return title_details

song_details = get_titles_lyrics()
title_details = extract_title_first_letters(song_details)
