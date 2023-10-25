def locate_ordered_lyric_subsets(small, large):
    matches_in_song = []  # List to store all matches
    # will turn first_letters_lyrics into one list with each letters as element of one list
    large = [item for sublist in large for item in sublist]
    len_small = len(small)
    # loop that iterates over the total length of the large list by the length of the small list at each iteration. The “+1” is there because Python’s range() function stops one number before the end.
    for i in range(len(large) - len_small + 1):
        # checks if the current slice of the large list is equal to the small list to confirm that small is an ordered subset of large. This is done by comparing the value of the indices. 
        if large[i:i+len_small] == small:
            # if true immedially returns the starting index and the ending index of the matching slice by calculating the i+the lengh of the small index to capture the end indices.
            matches_in_song.append([i, i+len_small])  # Add the match to the list
    return matches_in_song if matches_in_song else False  # Return all matches if any, else False