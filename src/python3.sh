#!/bin/bash
if command -v python3 &>/dev/null; then
    echo "Python 3 is installed."
else
    echo "Python 3 is not installed."
    echo "Opening Python download page..."
    if [[ "$OSTYPE" == "linux-gnu"* ]]; then
        xdg-open https://www.python.org/downloads/
    elif [[ "$OSTYPE" == "darwin"* ]]; then
        open https://www.python.org/downloads/
    elif [[ "$OSTYPE" == "cygwin" ]]; then
        cygstart https://www.python.org/downloads/
    elif [[ "$OSTYPE" == "msys" ]]; then
        start https://www.python.org/downloads/
    elif [[ "$OSTYPE" == "win32" ]]; then
        start https://www.python.org/downloads/
    else
        echo "Unable to open browser. Please manually navigate to https://www.python.org/downloads/"
    fi
fi