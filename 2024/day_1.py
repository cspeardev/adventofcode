#!/usr/bin/env python3
'''Day one of Advent of Code'''
import os
import time

start_time = time.time()

def get_index_of_lowest(array:list[int])-> int:
  lowest = min(array)
  return array.index(lowest)

script_dir = os.path.dirname(__file__)
input_file_path = script_dir + '/input/1'

first_array = []
second_array = []

with open(input_file_path,encoding='utf-8') as input_file:
  lines = [line for line in input_file]
  first_array = [int(line[0:5]) for line in lines]
  second_array = [int(line[8:]) for line in lines]

pairs = [()]*0
first_array_part_1 = first_array.copy()
second_array_part_1 = second_array.copy()

while len(first_array_part_1) > 0:
  first_lowest_index = first_array_part_1.index(min(first_array_part_1))
  second_lowest_index = second_array_part_1.index(min(second_array_part_1))
  pairs.append((first_array_part_1[first_lowest_index],
                second_array_part_1[second_lowest_index]))
  del first_array_part_1[first_lowest_index]
  del second_array_part_1[second_lowest_index]

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
