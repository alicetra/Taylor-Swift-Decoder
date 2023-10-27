#!/bin/bash
# This script will create a Python virtual environment

# Specify the directory for the virtual environment
venv_dir="myenv"

# Create the virtual environment
python3 -m venv $venv_dir

echo "Virtual environment created in directory $venv_dir."