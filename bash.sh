#!/bin/bash
# This is the main script

# Change to the src directory
cd src

# Ensure scripts have execute permissions
chmod a+x env.sh
chmod a+x python3.sh
chmod a+x requirement.sh

# Check if Python 3 is installed
./python3.sh

# If Python 3 is installed, create a virtual environment
if command -v python3 &>/dev/null; then
    ./env.sh
fi

# Activate the virtual environment
source myenv/bin/activate

# Check if the virtual environment is activated
if [[ "$VIRTUAL_ENV" != "" ]]; then
    # Install or update the specified Python packages
    ./requirement.sh

    # Run the main Python script for decoder
    python3 main.py

    # Deactivate the virtual environment
    deactivate
else 
    echo "Virtual environment is not activated. Skipping requirements installation."
fi