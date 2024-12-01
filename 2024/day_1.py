#!/usr/bin/env python3
'''Day one of Advent of Code'''
import collections
import os
import time

start_time = time.time()

script_dir = os.path.dirname(__file__)
input_file_path = script_dir + '/input/1'

first_array = []
second_array = []

with open(input_file_path,encoding='utf-8') as input_file:
  lines = [line for line in input_file]
  first_array = [int(line[0:5]) for line in lines]
  second_array = [int(line[8:]) for line in lines]

first_array.sort()
second_array.sort()

pairs = zip(first_array,second_array)

diffs = (abs(pair[0] - pair[1]) for pair in pairs)

sum_of_diffs = sum(diffs)

print('Solution for part one is ' + str(sum_of_diffs))

end_time = time.time()
elapsed_time = end_time - start_time
elapsed_time_in_milliseconds = elapsed_time * 1000
print('Elapsed time for part one: ' + str(elapsed_time_in_milliseconds))

# --- Part Two
start_time = time.time()

multiplied_numbers = [number * second_array.count(number)
                      for number in first_array]

similarity_score = sum(multiplied_numbers)

print('Solution for part two is ' + str(similarity_score))

end_time = time.time()
elapsed_time = end_time - start_time
elapsed_time_in_milliseconds = elapsed_time * 1000
print('Elapsed time for part two: ' + str(elapsed_time_in_milliseconds))
