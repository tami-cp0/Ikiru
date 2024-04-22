#!/usr/bin/python3

import os

# Get the current working directory
current_directory = os.getcwd()

if not current_directory.endswith("Ikiru"):
    print("run in ikiru directory")
    exit(1)
print(current_directory)