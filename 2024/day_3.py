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

# --- Part Two
# Same as above but identify 'do' or 'don't' in memory before operations

search_regex = r'(do\(\)|don\'t\(\))|mul\((\d*)\,(\d*)\)'

matches = regex.findall(search_regex,memory)

active = True
solution = 0

for match_type, value1, value2 in matches:
  if match_type:
    active = match_type == 'do()'
  else:
    if active:
      solution += int(value1) * int(value2)

print (f'Solution for part two is: {solution}')

end_time = time.time()
elapsed_time = end_time - start_time
elapsed_time_in_milliseconds = elapsed_time * 1000
print('Elapsed time for part two: ' + str(elapsed_time_in_milliseconds))
