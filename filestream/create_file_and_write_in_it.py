#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 19:31:26 2024

@author: gurkan
"""
###########################################################
from pathlib import Path

path = Path("/home/gurkan/coding/python/myScripts")

# Create the directory if it does not exist
path.mkdir(parents=True, exist_ok=True)

fileName = "create_file_and_write_in_it"

filePath = path / fileName

filePathExtended = filePath.with_suffix(".txt")

greetingText = "Hello World!"

with open(filePathExtended, 'w') as file:
    file.write(greetingText)
#############################################################

