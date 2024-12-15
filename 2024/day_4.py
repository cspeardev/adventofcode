#!/usr/bin/env python3
'''Day 4 of Advent of Code'''
import time
import utilities

def part_1(input_file_content:str):
  lines = input_file_content.splitlines()
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
  return match_count

def part_2(input_file_content:str):
  lines = input_file_content.splitlines()
  x_mas_count=0
  for y,line in enumerate(lines[1:-1],start=1):
    for x,character in enumerate(line[1:-1],start=1):
      if character == 'A':
        coordinates = [(x+1,y+1), (x+1,y-1), (x-1,y+1), (x-1,y-1)]
        values = [lines[c[1]][c[0]] for c in coordinates]
        slices = [''.join([values[i], 'A', values[-(i+1)]]) for i in range(2)]
        if all('MAS' == s or 'SAM' == s for s in slices):
          x_mas_count += 1
  return x_mas_count

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
