#!/usr/bin/env python3
'''Day 18 of Advent of Code'''
from collections import defaultdict, deque
import utilities
import time

def parse_fall_coordinates(input_file_content):
  coordinate_set=[]
  for line in input_file_content.splitlines():
    x,y = line.split(',')
    coordinate_set.append((int(x),int(y)))
  return tuple(coordinate_set)

def bfs(start, end, fall_coordinates):
  if start == end or start in fall_coordinates or end in fall_coordinates:
    return None
  queue = deque([start])
  visited = {start}
  parent = defaultdict(lambda: None)
  while queue:
    x, y = queue.popleft()
    if (x, y) == end:
      break
    for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
      next_pos = x + dx, y + dy
      if is_valid(next_pos,fall_coordinates,end) and next_pos not in visited:
        queue.append(next_pos)
        visited.add(next_pos)
        parent[next_pos] = (x, y)
  if end not in parent:
    return None
  path = reconstruct_path(start, end, parent)
  return path

def reconstruct_path(start, end, parent):
  path = [end]
  while path[-1] != start:
    path.append(parent[path[-1]])
  path.reverse()
  return path

def is_valid(position, fall_coordinates,end):
  return position not in fall_coordinates and (0 <= position[0] <= end[0]) and (0 <= position[1] <= end[0])

def part_1(input_file_content:str):
  all_fall_coordinates = parse_fall_coordinates(input_file_content)
  start=(0,0)
  end=(70,70)
  fall_coordinates=all_fall_coordinates[:1024]
  path = bfs(start,end,fall_coordinates)
  return len(path)-1

def part_2(input_file_content:str):
  all_fall_coordinates = parse_fall_coordinates(input_file_content)
  start=(0,0)
  end=(70,70)
  start_index=1024
  for i in range(len(all_fall_coordinates)-start_index):
    coordinates = all_fall_coordinates[:start_index+i]
    path = bfs(start,end,coordinates)
    if not path:
      return coordinates[-1]
  return None

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
