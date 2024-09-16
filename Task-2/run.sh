#!/bin/bash

echo "Installing dependencies..."
pip install -r requirements.txt

echo "Running unit tests..."
python -m unittest discover -s main/tests -p "*.py"

if [ $? -eq 0 ]; then
    echo "Tests passed successfully."
else
    echo "Tests failed."
    exit 1
fi

echo "Launching the main application..."
python main/main.py
