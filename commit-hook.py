#!/usr/bin/env python3

import os
import zipfile
import subprocess

# Directory where your .ork files are stored
ORK_DIR = 'path_to_your_ork_files'

def is_zip_file(filepath):
    return zipfile.is_zipfile(filepath)

# Loop over each file in the directory
for file in os.listdir(ORK_DIR):
    if file.endswith('.ork'):
        # Full path to the file
        file_path = os.path.join(ORK_DIR, file)

        # If the file is a zip file, unzip it and remove the zipped version
        if is_zip_file(file_path):
            # Unzip the file into the same directory
            with zipfile.ZipFile(file_path, 'r') as zip_ref:
                zip_ref.extractall(ORK_DIR)

            # Delete the zipped version of the file
            os.remove(file_path)
         

for file in os.listdir(ORK_DIR):
    if file.endswith('.ork'):
        # Full path to the file
        file_path = os.path.join(ORK_DIR, file)
        print("path:",file_path)
        # If the file is a zip file, unzip it and remove the zipped version
        if not is_zip_file(file_path):
            subprocess.run(['git', 'add', file_path])
