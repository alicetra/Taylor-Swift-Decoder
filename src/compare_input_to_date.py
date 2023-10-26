from extract_first_letters import title_details, lyrics_details
from ordered_subset import locate_ordered_lyric_subsets

def compare_input_to_data(letters):
    printed_titles = set()
    printed_lyrics = set()
    found_match = False

    # Compare input to title.
    for i in range(len(title_details)):
        if letters == title_details[i][1]:
            song_title = title_details[i][0].rstrip()
            if song_title not in printed_titles:
                print(f'\nTitle of Song: {song_title}\n')
                printed_titles.add(song_title)

    # Compare input to lyrics.
    for i in range(len(lyrics_details)):
        matches = locate_ordered_lyric_subsets(letters, lyrics_details[i][1])
        if matches:
            words = lyrics_details[i][0].split()
            # Loop through all matches.
            for match in matches: 
                # Print lyrics full words and joining them into a string. 
                lyrics = ' '.join(words[match[0]:match[1]])  
                if lyrics not in printed_lyrics:  
                    print(f"\nLyrics: {lyrics}")
                    print(f"Title of Song: {title_details[i][0]}\n")
                    printed_lyrics.add(lyrics)  
                    # Set the flag to True since a match was found.
                    found_match = True  
    # If no match was found after all iterations.
    if not found_match:  
        print("The abbreviation doesn't match any lyrics or song title")