# T1A3 Terminal Application 

[GitHub Repositority](https://github.com/alicetra/Taylor-Swift-Decoder)

# Application Features

**User Input:**  
User input can be in capital or lowercases and the terminal will print out corresponding full song titles or lyrics or both, according to the acronyms inputted.

**Identify Matching Acronyms in Song Titles:**  
The application is designed to match acronyms with song titles that are more than two words long. If an acronym matches a song title, the application will output the corresponding song title. This is because shorter song titles are likely to be spelled out entirely on a friendship bracelet, eliminating the need for decoding.

**Identify Matching Acronyms in Lyrics:**  
It can extract lyrics from any part of a song, and a line from the lyrics can be fetched from any section within the complete lyrics. The length of the lyrics acronym doesn’t matter. The system will attempt to decode it regardless of how long or short it is.

**Display Both Song Title and Corresponding Lyric:**  
If an acronym corresponds to a lyric from a song, the application will also display the title of the song from which the lyrics were derived.

**Prompt for Decoding Another Bracelet With No Matches Handling:**  
If the acronym on the bracelet doesn’t match any song titles or lyrics in the database, you’ll get a message saying so. You’ll then be asked if you want to try decoding another bracelet. Even if there is a match, you’ll still be asked if you want to decode another one.

**Error Handling for Invalid Inputs:**  
If anything else but a letter is inputted an error message will print out and it will reprompt again to ask if you wish to decode another acronym.

**Understanding ‘Yes’ or ‘No’ Inputs:**  
In terms of the prompt “Do you want to decode another acronym? (yes/no):”, users can input ‘yes’ or ‘no’ in Capital and it will still understand the input.

**Termination:**  
Only when ‘no’ or ‘NO’ is typed will the application terminate.

# Code Style Guide

I followed PEP8 styling guidelines and my code includes the below styles

**Imports:**  
Imports are on separate lines 

**Indentation:**  
Code uses 4 spaces for indentation

**Line Length:**  
None of the lines in the code exceed the recommended maximum line length of 79 characters.

**Variable Names:**  
The variable names are descriptive and use lowercase with words separated by underscores as recommended.

**Modules (filenames):**  
They all have short, all-lowercase names, and they can contain underscores

**Comments:**  
Comments are complete sentences and end with a period. Also, start with a # and a single space. They should be indented to the same level as the code they are commenting

**Function Names:**  
Function names are lowercase, with words separated by underscores as necessary to improve readability.

**Function Space:**  
According to PEP8 style guide, there should be two blank lines between functions or classes.

# System/Hardware requirements 
Bash script for installment of application requires Unix-like systems (such as Linux and macOS)  
The application was coded in Python 3.10.12.  
Python installation requires operating system: Linux- Ubuntu 16.04 to 17.10, or Windows 7 to 10, with minimum 2GB RAM (4GB preferable) 

# Installation 

**Fetch the Project from GitHub:**  
First, you’ll need to clone the project repository from GitHub to your local system. You can do this by using the git clone command followed by the URL of the repository. eg: git clone https://github.com/alicetra/Taylor-Swift-Decoder.git.

**Navigate to the Project Directory:**  
Once you have cloned the repository, use the cd command to navigate into the project directory. For example, if my project is named “Taylor-Swift-Decoder”, you would type cd Taylor-Swift-Decoder.

**Grant Execute Permission:**  
Next, type chmod a+x bash.sh in the terminal and press enter. This command gives all users on your system the permission to execute your script.

**Run the Script:**  
Finally, you can run your script by typing ./bash.sh in the terminal and pressing enter.

# Dependencies  
beautifulsoup4     4.12.2  
certifi            2023.7.22  
charset-normalizer 3.3.0  
exceptiongroup     1.1.3  
idna               3.4  
iniconfig          2.0.0  
lyricsgenius       3.0.1  
packaging          23.2  
pip                22.0.2  
pluggy             1.3.0  
pytest             7.4.3  
requests           2.31.0  
setuptools         59.6.0  
soupsieve          2.5  
tomli              2.0.1  
urllib3            2.0.6  

# How to use 

**User Input:**  
When prompted, enter your friendship bracelet letters. The input should be all letters; if it’s not, you’ll receive an error message “Input has to be all letters”. The input is case-insensitive.

**Output:**  
The script will compare your input to the song titles and lyrics in the database. If a match is found, it will print the song title and the corresponding lyrics. If no match is found, it will print a message indicating that no match was found.

**Decoding Another Acronym:**  
After each comparison, you’ll be asked if you want to decode another acronym. Enter ‘yes’ or ‘no’. The input is case-insensitive.If you enter anything other than ‘yes’ or ‘no’, you’ll receive an error message “Characters other than ‘yes’ or ‘no’ was typed.” Once error message is display it will once more ask you if you wish to decode another acronym.

**Termination:**  
If you wish to terminate application input ‘no’ once prompt to ask if you wish to decode another acronym is on terminal. The input is case-insensitive.

# Pytests

In order to run the pytests, after installation you need to run the following command on the terminal 

source src/myenv/bin/activate  
pytest 

**test_user_input**  

I ran a pytest to ensure that my error handling for user_input was solid. My decoding will not work if user_input is not working as expected. It is the start and foundation of my application 

- test_user_input() with input “123”:  
 This test checks if the user_input function correctly handles numeric input. The function is expected to return the message “Input has to be all letters” when the input is not all letters. This test is important to ensure that the function can correctly handle and respond to invalid input.

- test_user_input() with input “a1d”:  
 This test checks if the user_input function correctly handles alphanumeric input. Similar to the first test, the function is expected to return the message “Input has to be all letters”. This test is important to ensure that the function can correctly handle and respond to invalid input that contains both letters and numbers.  

- test_user_input() with input “abc!”: 
 This test checks if the user_input function correctly handles input that includes special characters. The function is expected to return the message “Input has to be all letters”. This test is important to ensure that the function can correctly handle and respond to invalid input that contains special characters.

- test_user_input() with input “abc”:  
 This test checks if the user_input function correctly handles valid lowercase alphabetic input. The function is expected to return [‘A’, ‘B’, ‘C’], which are the uppercase versions of the input letters. This test is important to ensure that the function can correctly process valid lowercase alphabetic input.

- test_user_input() with input “aBc”:  
 This test checks if the user_input function correctly handles valid mixed-case alphabetic input. The function is expected to return [‘A’, ‘B’, ‘C’], which are the uppercase versions of the input letters. This test is important to ensure that the function can correctly process valid mixed-case alphabetic input.

**test_extract_first_letters**  

I ran a pytest to ensure that my function  ‘extract_first_letters.py’, was correctly pulling the first letter from each word. This was crucial because my decoding mechanism relies on matching the user’s input with entries in the database. To make this match, I had to pull out the first letter from each word in the database entries

**test_ordered_subset**  

Conducting a pytest for the ‘ordered_subset’ function was essential. I had to validate several logical aspects because the decoding of lyrics depended on this function. It was responsible for identifying and returning the complete lyrics based on acronyms. This was key to the success of my feature that could extract lyrics from any section of a song.

- test_locate_ordered_lyric_subsets_indices_match():  
 This test checks if the function locate_ordered_lyric_subsets can correctly identify a match. The ‘small’ list is [‘h’, ‘e’, ‘l’, ‘l’, ‘o’], which matches the first five elements of the ‘large’ list. The expected output is [[0, 5]], indicating the start and end indices of the match in the ‘large’ list. This test is important to ensure that the function can correctly return the indices that correspond to the position where the letters matches are found. 

- test_locate_ordered_lyric_subsets_no_matches():  
 This test checks if the function correctly returns False when there are no matches between the ‘small’ and ‘large’ lists.This test is important to ensure that the function can correctly handle cases where there are no matches.

- test_locate_ordered_lyric_subsets_no_match_due_to_order():  
 This test checks if the function correctly returns False when the elements in the ‘small’ list appear in a different order in the ‘large’ list. The ‘small’ list is [‘e’, ‘h’, ‘l’, ‘l’, ‘o’], which contains all elements in the first five elements of the ‘large’ list but in a different order. This test is important to ensure that the function considers the order of elements when identifying matches.

- test_locate_ordered_lyric_subsets_middle_match():  
This test checks if the function can correctly identify a match in the middle of the ‘large’ list. The ‘small’ list is [‘o’, ‘r’, ‘l’], which matches elements 6 to 9 in the ‘large’ list. The expected output is [[6, 9]], indicating the start and end indices of the match in the large list. This test is important to ensure that the function can correctly identify matches that are not only at the start of the list.

# Implementation Plan

**19/10/2023**  
![Alt text](docs/Trello19102023.PNG)
![Alt text](docs/19102023-part1.PNG)
![Alt text](docs/191022023-part2.PNG) 
![Alt text](docs/19102023-part3.PNG)  
![Alt text](docs/191022023-part4.PNG)  
![Alt text](docs/19102023-part5.PNG)  
![Alt text](docs/191022023-part5.PNG)  
![Alt text](docs/Trello19102023end.PNG)  
**20/10/2023**   
![Alt text](docs/Trello20102023.PNG)  
![Alt text](docs/Trello20102023-part1.PNG)  
![Alt text](docs/Trello20102023-end.PNG)  

**23/10/2023**   
![Alt text](docs/trello23102023.PNG)  
![Alt text](docs/trello23102023-part1.PNG)  
![Alt text](docs/trello2023102023-end.PNG)  
**24/10/2023**  
![Alt text](docs/Trello24102023.PNG)  
![Alt text](docs/trello24102023part-1.PNG)  
![Alt text](docs/trello24102023-end.PNG)  
**25/10/2023**   
![Alt text](docs/Trello25102023.PNG)  
![Alt text](docs/25102023-part1.PNG)  
![Alt text](docs/trello25102023-midday.PNG)  
![Alt text](docs/trello25102023-part2.PNG)  
![Alt text](docs/trello25102023-part3.PNG)  
![Alt text](docs/trello25102023-end.PNG)  
**26/10/2023**  
![Alt text](docs/Trello26102023.PNG)  
![Alt text](docs/trello26102023-part1.PNG)  
![Alt text](docs/trello26102023-part2.PNG)  
![Alt text](docs/trello26102023-part3.PNG)  
![Alt text](docs/trello26102023-end.PNG)  
**27/10/2023**  
![Alt text](docs/trello27102023.PNG)  
![Alt text](docs/trello27102023-part1.PNG)  
![Alt text](docs/trello27102023-part2.PNG)  
![Alt text](docs/trello27102023-end.PNG)  

# Reference sources
- Van Rossum, G., Warsaw, B. and Coghlan, N. (2001). PEP 8 – Style Guide for Python Code | peps.python.org.  
  Available at: https://peps.python.org/pep-0008/.
- LyricsGenius: a Python client for the Genius.com API — lyricsgenius documentation.  
  Available at: https://lyricsgenius.readthedocs.io/en/master/.
- Instructions to install Python 3. (n.d.).  
Available at: https://www.shahandanchor.com/home/wp-content/uploads/Python-installation-instructions-1.pdf.
