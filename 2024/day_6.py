#!/usr/bin/env python3
'''Day six of Advent of Code'''
import time
import os

def walk_obstacles(width, height, start, obstacles):
  visited_positions=[]*0
  directions=[(-1,0),(0,1),(1,0),(0,-1)]
  current_direction = directions[0]
  current_position = start
  while(0 <= current_position[0] <= width
    and 0 <= current_position [1] <= height):
    if current_position not in visited_positions:
      visited_positions.append(current_position)
    next_position = (current_position[0]+current_direction[0],
                  current_position[1]+current_direction[1])
    if next_position in obstacles:
      current_direction_index = directions.index(current_direction)
      next_direction_index = (current_direction_index+1) % len(directions)
      current_direction=directions[next_direction_index]
      next_position = (current_position[0]+current_direction[0],
                  current_position[1]+current_direction[1])
    current_position = next_position
  return visited_positions

def walk_obstacles_find_loop(width, height, start, obstacles):
  visited_positions=set()
  directions=[(-1,0),(0,1),(1,0),(0,-1)]
  current_direction = directions[0]
  current_position = start
  while(0 <= current_position[1] <= width
    and 0 <= current_position [0] <= height):
    if current_position not in visited_positions:
      visited_positions.add((current_position,current_direction))
    next_position = (current_position[0]+current_direction[0],
                  current_position[1]+current_direction[1])
    if next_position in obstacles:
      current_direction_index = directions.index(current_direction)
      next_direction_index = (current_direction_index+1) % len(directions)
      current_direction=directions[next_direction_index]
      next_position = (current_position[0]+current_direction[0],
                  current_position[1]+current_direction[1])
    current_position = next_position
    if (current_position,current_direction) in visited_positions:
      return True
  return False



def main():
  script_dir = os.path.dirname(__file__)
  input_file_path = script_dir + '/input/6'

  with open(input_file_path,encoding='utf-8') as input_file:
    lines = [line.strip() for line in input_file]

  part_1_start_time = time.time()
  part_1_solution = part_1(lines)
  part_1_end_time = time.time()
  print(f'Solution for part 1: {part_1_solution}')

  part_1_elapsed_time = part_1_end_time - part_1_start_time
  elapsed_time_in_milliseconds = part_1_elapsed_time * 1000
  print(f'Elapsed time for part 1: {str(elapsed_time_in_milliseconds*1000)} ms')

  part_2_start_time = time.time()
  part_2_solution = part_2(lines)
  part_2_end_time = time.time()
  print(f'Solution for part 2: {part_2_solution}')

  part_2_elapsed_time = part_2_end_time - part_2_start_time
  elapsed_time_in_milliseconds = part_2_elapsed_time * 1000
  print(f'Elapsed time for part 2: {str(elapsed_time_in_milliseconds*1000)} ms')


def part_1(lines):
  starting_position = (0,0)

  for i, line in enumerate(lines):
    if '^' in line:
      starting_position = (i,line.index('^'))

  obstacle_coordinates= find_obstacles(lines)

  lines_width=len(lines[0])
  lines_height=len(lines)
  solution=len(walk_obstacles(lines_width, lines_height , starting_position, obstacle_coordinates))-1
  return solution


def part_2(lines):
  solution=0
  starting_position = (0,0)
  for i, line in enumerate(lines):
    if '^' in line:
      starting_position = (i,line.index('^'))

  obstacle_coordinates = find_obstacles(lines)

  lines_width=len(lines[0])
  lines_height=len(lines)

  for i,line in enumerate(lines):
    for j,letter in enumerate (line):
      if (i,j) not in obstacle_coordinates and (i,j) != starting_position:
        temp_obstacle_coordinates = obstacle_coordinates.copy()
        temp_obstacle_coordinates.add((i,j))
        if walk_obstacles_find_loop(lines_width, lines_height, starting_position, temp_obstacle_coordinates):
          solution += 1

  return solution

def find_obstacles(lines):
  obstacle_coordinates=set()
  for i, line in enumerate(lines):
    if '#' in line:
      coordinates = [j for j, letter in enumerate(line) if letter == '#']
      for j in coordinates:
        obstacle_coordinates.add((i, j))
  return obstacle_coordinates

if __name__ == '__main__':
  main()
