#!/usr/bin/env python3
'''Day three of Advent of Code'''
import os
import time
import regex

# --- Part One
# Extract multiply functions from corrupted string. Multiply functions will be
# in the form of 'mul(x,x)'

start_time = time.time()

script_dir = os.path.dirname(__file__)
input_file_path = script_dir + '/input/3'

memory=''

with open(input_file_path,encoding='utf-8') as input_file:
  memory = '\n'.join([line.strip() for line in input_file])

search_regex = r'\bmul\b\((\d*)\,(\d*)\)'

matches = regex.findall(search_regex,memory)

solution = sum([int(pair[0]) * int(pair[1]) for pair in matches ])

print (f'Solution for part one is: {solution}')

end_time = time.time()
elapsed_time = end_time - start_time
elapsed_time_in_milliseconds = elapsed_time * 1000
print('Elapsed time for part one: ' + str(elapsed_time_in_milliseconds))
