# Automated-url-opener

## Overview

The `Automated-url-opener` is a simple tool that automatically opens all the links listed in a text document file named "url". This can help streamline your workflow by decluttering your browser and automatically opening important URLs every time you start your work. 

## Instructions

1. Create a text file named "url". The file has to be named "url" for the program to work. 
2. Copy and paste the URLs that you want to automatically open in your browser into the "url" text file. Each URL should be on a separate line.
3. Run the executable file `Automated-url-opener.exe`. It will read the URLs from the "url" text file and open them in your default web browser.

## Build Instructions

If you want to build your own executable file from the Python script uploaded in this repository, you can do so using the following steps:

1. Install the `pyinstaller` package by running `pip install pyinstaller`.
2. Navigate to the directory containing the Python script (`Automated-url-opener.py`) in the command line.
3. Run the command `pyinstaller --onefile "Automated-url-opener.py"`. The `--onefile` option creates a standalone executable file.

## Note

Make sure to keep the "url" text file and the executable file (`Automated-url-opener.exe`) in the same directory for proper functioning.
