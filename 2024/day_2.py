#!/usr/bin/env python3
'''Day two of Advent of Code'''
import os
import time


# --- Part Two
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

safe_count = 0

for reading in readings:
  is_safe = True
  if len(reading) == 1:
    break
  last_value:int = reading[0]

  increasing = False
  decreasing = False

  if reading[0] < reading[1]:
    increasing = True
  elif reading[0] > reading[1]:
    decreasing = True
  else:
    continue

  for value in reading[1:]:

    diff = value - last_value

    if (increasing and diff < 1
        or decreasing and diff > -1
        or diff == 0):
      is_safe = False
      break

    diff = abs(diff)
    if not 1 <= diff <= 3:
      is_safe = False
      break
    last_value = value

  if is_safe:
    safe_count += 1

print(f"Solution for part one is {safe_count}")

end_time = time.time()
elapsed_time = end_time - start_time
elapsed_time_in_milliseconds = elapsed_time * 1000
print('Elapsed time for part one: ' + str(elapsed_time_in_milliseconds))
