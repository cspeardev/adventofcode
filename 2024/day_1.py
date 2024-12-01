#!/usr/bin/env python3
'''Day one of Advent of Code'''
import os
import time

start_time = time.time()

def get_index_of_lowest(array:[])-> int:
  lowest_index = 0
  lowest = array[lowest_index]
  for i in enumerate(array):
    index = i[0]
    value = i[1]
    if value < lowest:
      lowest_index = index
      lowest = array[lowest_index]
  return lowest_index

script_dir = os.path.dirname(__file__)
input_file_path = script_dir + '/input/1'

first_array = []
second_array = []

with open(input_file_path,encoding='utf-8') as input_file:
  for line in input_file:
    first = int(line[0:5])
    second = int(line[8:])
    first_array.append(first)
    second_array.append(second)

pairs = [()]*0

while len(first_array) > 0:
  first_lowest_index = get_index_of_lowest(first_array)
  second_lowest_index = get_index_of_lowest(second_array)
  pairs.append((first_array[first_lowest_index],
                second_array[second_lowest_index]))
  del first_array[first_lowest_index]
  del second_array[second_lowest_index]

diffs = []

for pair in pairs:
  diffs.append(abs(pair[0]-pair[1]))

sum_of_diffs = sum(diffs)

print('Solution is ' + str(sum_of_diffs))

end_time = time.time()
elapsed_time = end_time - start_time
elapsed_time_in_milliseconds = elapsed_time * 1000
print('Elapsed time: ' + str(elapsed_time_in_milliseconds))
