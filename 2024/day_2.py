#!/usr/bin/env python3
'''Day two of Advent of Code'''
import os
import time

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

# --- Part One
# Data sets are safe if values are all descending or all ascending and the
# difference between each value is between 1 and 3. Solution is to find the
# count of all readings that are safe.

start_time = time.time()

script_dir = os.path.dirname(__file__)
input_file_path = script_dir + '/input/2'

readings = [[]]

with open(input_file_path,encoding='utf-8') as input_file:
  lines = [line.strip() for line in input_file]
  readings = [[int(value) for value in str.split(line,' ')] for line in lines]

safe_count = sum(is_reading_set_safe(reading) for reading in readings.copy())
print(f"Solution for part one is {safe_count}")

end_time = time.time()
elapsed_time = end_time - start_time
elapsed_time_in_milliseconds = elapsed_time * 1000
print('Elapsed time for part one: ' + str(elapsed_time_in_milliseconds))

# --- Part Two
# Same logic as above, however need to implement a 'Problem Dampener', which
# allows for a single bad reading in a set.
start_time = time.time()

safe_count = sum(is_reading_set_safe(reading)
                 or any(is_reading_set_safe([v for i,
                                             v in enumerate(reading) if i != j])
                                             for j in range(len(reading)))
                                             for reading in readings)

print(f"Solution for part two is {safe_count}")

end_time = time.time()
elapsed_time = end_time - start_time
elapsed_time_in_milliseconds = elapsed_time * 1000
print('Elapsed time for part two: ' + str(elapsed_time_in_milliseconds))
