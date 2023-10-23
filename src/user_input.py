def user_input():
        letters_to_decode = input("Please enter your friendship bracelet letters: ")
        # Converting each letter from user input to a list
        letters_to_decode_list = list(letters_to_decode)
        # Make sure that the input will be converted to upper case so that it will match title_details format
        letters_to_decode_list = [letter.upper() for letter in letters_to_decode_list]
        print(letters_to_decode_list)
        return letters_to_decode_list

user_input()
