#!/bin/bash

# check if Python3 exists
command -v python3 >/dev/null 2>&1 || { echo "Python3 was not found. Exiting..."; exit 1; }
# check if ffmpeg 
command -v ffmpeg >/dev/null 2>&1 || { echo "ffmpeg was not found. Exiting..."; exit 1; }

# build the script and install it
python3 setup.py build && python3 setup.py install