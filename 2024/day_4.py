#!/usr/bin/env python3
'''Day four of Advent of Code'''
import time
import os

# --- Part one
# Input is wordsearch, find all isntances of XMAS
start_time = time.time()

script_dir = os.path.dirname(__file__)
input_file_path = script_dir + '/input/4'

with open(input_file_path,encoding='utf-8') as input_file:
  lines = [line.strip() for line in input_file]

match_count = 0
height = len(lines)
width = len(lines[0])
match = 'XMAS'
match_length = len(match)

for line in enumerate(lines):
  y = line[0]
  for characters in enumerate(line[1]):
    x = characters[0]
    directions = [(1, 0), (1, -1), (0, -1),(-1, -1),
                  (-1, 0), (-1, 1), (0, 1), (1, 1)]
    coordinates_set = [[(x + i*dx, y + i*dy)
                        for i in range(match_length)]
                        for dx, dy in directions]
    for coordinates in coordinates_set:
      if (0 <= coordinates[match_length-1][0] < width
              and 0 <= coordinates[match_length-1][1] <= height-1):
        word = ''.join([lines[x_coord][y_coord]
                        for x_coord,y_coord in coordinates])
        if word == match:
          match_count += 1

print(f'Solution for part one is {match_count}')

end_time = time.time()
elapsed_time = end_time - start_time
elapsed_time_in_milliseconds = elapsed_time * 1000
print('Elapsed time for part one: ' + str(elapsed_time_in_milliseconds))


# # --- Part Two
start_time = time.time()
x_mas_count=0

for y,line in enumerate(lines[1:-1],start=1):
  for x,character in enumerate(line[1:-1],start=1):
    if character == 'A':
      coordinates = [(x+1,y+1), (x+1,y-1), (x-1,y+1), (x-1,y-1)]
      values = [lines[c[1]][c[0]] for c in coordinates]
      slices = [''.join([values[i], 'A', values[-(i+1)]]) for i in range(2)]

      if all('MAS' == s or 'SAM' == s for s in slices):
        x_mas_count += 1

print(f'The solution for part two is {x_mas_count}')

end_time = time.time()
elapsed_time = end_time - start_time
elapsed_time_in_milliseconds = elapsed_time * 1000
print('Elapsed time for part one: ' + str(elapsed_time_in_milliseconds))
