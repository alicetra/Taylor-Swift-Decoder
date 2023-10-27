from reading_jsonfile import get_titles_lyrics
from user_input import user_input
from extract_first_letters import extract_lyric_first_letters, extract_title_first_letters
from compare_input_to_date import compare_input_to_data

try:
    song_details = get_titles_lyrics()
    title_details = extract_title_first_letters(song_details)
    lyrics_details = extract_lyric_first_letters(song_details)
    continue_decoding = "YES"
    while continue_decoding.upper() == "YES":
        try:
            letters = user_input()
            if letters is not None:
                compare_input_to_data(letters)
        except ValueError as e:
            print(e)
            continue
        while True:
            try:
                continue_decoding = input("Do you want to decode another acronym? (yes/no): ")
                if continue_decoding.upper() not in ["YES", "NO"]:
                    raise ValueError("Invalid input")
                break
            except ValueError:
                print("Characters others than 'yes' or 'no' was typed.")
except Exception as e:
    print(f"An error occurred: {e}")