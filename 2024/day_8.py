#!/usr/bin/env python3
'''Day 8 of Advent of Code'''
import utilities
import time

def part_1(input_file_content:str):
  lines = input_file_content.splitlines()
  antinodes=set()
  all_antennas=find_antennas(lines)
  width=len(lines[0])+1
  height=len(lines)+1

  for frequency_antennas in all_antennas.values():
    if len(frequency_antennas) > 1:
      for antenna in frequency_antennas:
        for temp_antenna in frequency_antennas:
          if antenna==temp_antenna:
            continue
          antinode=get_next_point(antenna,temp_antenna)
          if is_antinode_valid(width, height, antinode):
            if antinode not in antinodes:
              antinodes.add(antinode)
  return len(antinodes)

def is_antinode_valid(width, height, antinode):
  return 0 < antinode[1] <= width-1 and 0 < antinode[0] <=  height-1

def part_2(input_file_content:str):
  lines = input_file_content.splitlines()
  antinodes=set()
  all_antennas=find_antennas(lines)
  width=len(lines[0])+1
  height=len(lines)+1

  for frequency_antennas in all_antennas.values():
    if len(frequency_antennas) > 1:
      for antenna in frequency_antennas:
        if antenna not in antinodes:
          antinodes.add(antenna)
        for temp_antenna in frequency_antennas:
          if antenna==temp_antenna:
            continue
          point1 = antenna
          point2 = temp_antenna
          antinode=get_next_point(point1,point2)
          while is_antinode_valid(width, height, antinode):
            if antinode not in antinodes:
              antinodes.add(antinode)
            point1=point2
            point2=antinode
            antinode=get_next_point(point1,point2)
  return len(antinodes)

def get_next_point(point1,point2):
  x1, y1 = point1
  x2, y2 = point2
  m = (y2 - y1) / (x2 - x1)
  b = y1 - m * x1
  if m > 1:
    xdiff = x2-x1
    nx=x2+xdiff
    ny = (m*nx) + b
  else:
    ydiff=y2-y1
    ny=y2+ydiff
    nx = (ny-b)/m
  return (int(round(nx)), int(round(ny)))

def find_antennas(lines):
  antennas={}
  height=len(lines)
  for i,line in enumerate(lines):
    for j,character in enumerate(line):
      if character != '.':
        if character not in antennas:
          antennas[character]=set()
        antennas[character].add(((j+1),height-(i)))
  return antennas

def get_slope(point1,point2):
  return (point2[1]-point1[1])/(point2[0]-point1[0])

def get_y_intercept(slope,point):
  return point[0]-(slope*point[1])

def get_distance(point1,point2):
  return (point2[1]-point1[1])**2 + (point2[0]-point1[0])**2


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

