import pytest
from unittest.mock import patch
from extract_first_letters import extract_title_first_letters, extract_lyric_first_letters

@patch('extract_first_letters.text_formatting')
def test_extract_title_first_letters(mock_text_formatting):
    # Define the song details and expected output.
    song_details = [('all too well', 'lyrics')]
    expected_output = [['ALL TOO WELL', ['A', 'T', 'W']]]
    
    # Set the return value of the mocked function.
    mock_text_formatting.return_value = ('ALL TOO WELL', ['ALL', 'TOO', 'WELL'])
    
    # Call the function and check its output.
    assert extract_title_first_letters(song_details) == expected_output

@patch('extract_first_letters.text_formatting')
def test_extract_lyric_first_letters(mock_text_formatting):
    # Define the song details and expected output.
    song_details = [('title', 'cause here we are again')]
    expected_output = [['CAUSE HERE WE ARE AGAIN', [['C'], ['H'], ['W'], ['A'], ['A']]]]
    # Set the return value of the mocked function.
    mock_text_formatting.return_value = ('CAUSE HERE WE ARE AGAIN', ['CAUSE', 'HERE', 'WE', 'ARE', 'AGAIN'])
    # Call the function and check its output.
    assert extract_lyric_first_letters(song_details) == expected_output