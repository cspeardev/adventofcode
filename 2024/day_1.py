#!/usr/bin/env python3
'''Day one of Advent of Code'''
from collections import defaultdict
import utilities
import time
import pyperf

def part_1(input_file_content:str):
  first_array = []
  second_array = []

  lines = input_file_content.splitlines()
  first_array = [int(line[0:5]) for line in lines]
  second_array = [int(line[-5:]) for line in lines]

  first_array.sort()
  second_array.sort()

  pairs = zip(first_array,second_array)

  diffs = (abs(pair[0] - pair[1]) for pair in pairs)

  return sum(diffs)

def part_2(input_file_content:str):
  lines = input_file_content.splitlines()
  first_array = [int(line[0:5]) for line in lines]
  second_array = [int(line[-5:]) for line in lines]
  multiplied_numbers = []

  count_dict = defaultdict(int)
  for num in second_array:
    count_dict[num] += 1

  for num in first_array:
    multiplied_numbers.append(num * count_dict[num])

  return sum(multiplied_numbers)

def main():
  input_file_content = utilities.get_input_file_content()

  part_1_start_time = time.time()
  part_1_solution=part_1(input_file_content)
  part_1_end_time = time.time()

  print(f'Solution for part 1: {part_1_solution}')
  part_1_elapsed_time = part_1_end_time - part_1_start_time
  print(f'Elapsed time for part 1: {str(part_1_elapsed_time*1000)}')

  part_2_start_time = time.time()
  part_2_solution=part_2(input_file_content)
  part_2_end_time = time.time()

  print(f'Solution for part 2: {part_2_solution}')
  part_2_elapsed_time = part_2_end_time - part_2_start_time
  print(f'Elapsed time for part 2: {str(part_2_elapsed_time*1000)}')

if __name__ == '__main__':
  main()

