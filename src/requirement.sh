#!/bin/bash
# This script will install or update the specified Python packages

# List your packages here
packages="beautifulsoup4==4.12.2 certifi==2023.7.22 charset-normalizer==3.3.0 exceptiongroup==1.1.3 idna==3.4 iniconfig==2.0.0 lyricsgenius==3.0.1 packaging==23.2 pluggy==1.3.0 pytest==7.4.3 requests==2.31.0 soupsieve==2.5 tomli==2.0.1 urllib3==2.0.6"

# Loop through the packages and install or update them
for p in $packages; do
    echo "Installing/updating $p"
    python3 -m pip install --upgrade $p
done

echo "All packages have been installed or updated successfully."