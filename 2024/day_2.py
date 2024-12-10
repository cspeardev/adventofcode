#!/usr/bin/env python3
'''Day 2 of Advent of Code'''
import time
import utilities

def is_reading_set_safe(reading_set: list[int]) -> bool:
  if len(reading_set) == 1:
    return True
  last_value = reading_set[0]

  increasing = reading_set[0] < reading_set[1]
  decreasing = reading_set[0] > reading_set[1]

  for reading in reading_set[1:]:
    diff = reading - last_value

    if (increasing and diff < 1
        or decreasing and diff > -1
        or diff == 0):
      return False

    diff = abs(diff)
    if not 1 <= diff <= 3:
      return False
    last_value = reading
  return True

def part_1(input_file_content:str):
  lines = input_file_content.splitlines()
  readings = [[int(value) for value in str.split(line,' ')] for line in lines]

  return sum(is_reading_set_safe(reading) for reading in readings.copy())

def part_2(input_file_content:str):
  lines = input_file_content.splitlines()
  readings = frozenset(tuple(int(value) for value in str.split(line,' ')) for line in lines)
  return sum(is_reading_set_safe(reading)
             or any(is_reading_set_safe([v for i,
                                         v in enumerate(reading) if i != j])
                                         for j in range(len(reading)))
                                         for reading in readings)

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
