import pytest
from unittest.mock import patch
from io import StringIO
from contextlib import redirect_stdout
from user_input import user_input

def test_user_input():
    with patch('builtins.input', return_value="123"):
        f = StringIO()
        with redirect_stdout(f):
            user_input()
        output = f.getvalue().strip()
        assert output == "Input has to be all letters"

    with patch('builtins.input', return_value="a1d"):
        f = StringIO()
        with redirect_stdout(f):
            user_input()
        output = f.getvalue().strip()
        assert output == "Input has to be all letters"
    
    with patch('builtins.input', return_value="abc!"):
        f = StringIO()
        with redirect_stdout(f):
            user_input()
        output = f.getvalue().strip()
        assert output == "Input has to be all letters"

    with patch('builtins.input', return_value="abc"):
            result = user_input()
            assert result == ['A', 'B', 'C']
            
    with patch('builtins.input', return_value="aBc"):
        result = user_input()
        assert result == ['A', 'B', 'C']