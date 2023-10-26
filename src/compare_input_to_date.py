from extract_first_letters import title_details, lyrics_details

def compare_input_to_data(letters):
    printed_titles = set()

    # Compare input to title.
    for i in range(len(title_details)):
        if letters == title_details[i][1]:
            # Added the rstrip to remove duplicates in printed_titles I noticed.
            song_title = title_details[i][0].rstrip()
            if song_title not in printed_titles:
                print(f'\nTitle of Song: {song_title}\n')
                printed_titles.add(song_title)
