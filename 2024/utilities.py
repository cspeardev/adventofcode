#!/usr/bin/env python3
'''Common utilities for AOC 2024'''

import os
import sys

def get_input_file() -> str:
  script_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
  _, filename = os.path.split(sys.argv[0])
  day_number = filename[4:-3]
  input_file_path = os.path.join(script_dir, 'input', day_number)
  return input_file_path

def get_input_file_content() -> str:
  with open(get_input_file(),encoding='utf-8') as input_file:
    return input_file.read()
