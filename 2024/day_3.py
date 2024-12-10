#!/usr/bin/env python3
'''Day three of Advent of Code'''
import time
import regex
import utilities

def part_1(input_file_content):
  lines = input_file_content.splitlines()
  memory = '\n'.join([line.strip() for line in lines])
  search_regex = r'mul\((\d{1,3})\,(\d{1,3})\)'
  matches = regex.findall(search_regex,memory)
  return sum(int(val1) * int(val2) for val1,val2 in matches)

def part_2(input_file_content):
  memory = input_file_content
  search_regex = r'(do\(\)|don\'t\(\))|mul\((\d{1,3})\,(\d{1,3})\)'
  matches = regex.findall(search_regex,memory)
  active = True
  solution = 0
  for match_type, value1, value2 in matches:
    if match_type:
      active = match_type == 'do()'
    else:
      if active:
        solution += int(value1) * int(value2)
  return solution

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
