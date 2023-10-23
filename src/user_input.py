def user_input():
        letters_to_decode = input("Please enter your friendship bracelet letters: ")
        # Converting each letter from user input to a list
        letters_to_decode_list = list(letters_to_decode)
        print(letters_to_decode_list)
        return letters_to_decode_list

user_input()
