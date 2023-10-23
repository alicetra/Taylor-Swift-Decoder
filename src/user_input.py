def user_input():
    try:
        letters_to_decode = input("Please enter your friendship bracelet letters: ")
        # Converting each letter from user input to a list
        letters_to_decode_list = list(letters_to_decode)
        # Make sure that the input will be converted to upper case so that it will match title_details format
        letters_to_decode_list = [letter.upper() for letter in letters_to_decode_list]
        # Check if input list element are all letters if not true then an exception error will be raised
        if not all(item.isalpha() for item in letters_to_decode_list):
            raise ValueError("Input has to be all letters")
    except ValueError as e:
        print(e)
        return None
    return letters_to_decode_list