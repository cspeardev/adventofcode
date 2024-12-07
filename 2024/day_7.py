#!/usr/bin/env python3
'''Day 7 of Advent of Code'''
import itertools
import time
import os

def main():
  script_dir = os.path.dirname(__file__)
  input_file_path = script_dir + '/input/7'

  with open(input_file_path,encoding='utf-8') as input_file:
    puzzle_input = input_file.read()

  part_1_start_time = time.time()
  part_1_solution = part_1(puzzle_input)
  part_1_end_time = time.time()
  print(f'Solution for part 1: {part_1_solution}')

  part_1_elapsed_time = part_1_end_time - part_1_start_time
  print(f'Elapsed time for part 1: {str(part_1_elapsed_time*1000)} ms')

  part_2_start_time = time.time()
  part_2_solution = part_2(puzzle_input)
  part_2_end_time = time.time()
  print(f'Solution for part 2: {part_2_solution}')

  part_2_elapsed_time = part_2_end_time - part_2_start_time
  print(f'Elapsed time for part 2: {str(part_2_elapsed_time*1000)} ms')

def part_1(puzzle_input:str):
  solution=0
  parsed_lines = parse_lines(puzzle_input)
  for result,numbers in parsed_lines:
    operator_count=len(numbers)-1
    operator_permutations=get_permutations(operator_count)
    for operator_set in operator_permutations:
      operator_set_result = numbers[0]
      for operator_index,operator in enumerate(operator_set):
        if operator == '+':
          operator_set_result += numbers[operator_index+1]
        elif operator == '*':
          operator_set_result *= numbers[operator_index+1]
      if operator_set_result == result:
        solution += operator_set_result
        break
  return solution

def parse_lines(puzzle_input) -> set[tuple[int, tuple[int]]]:
  parsed_lines=set()
  for line in puzzle_input.splitlines():
    line_split = line.split(': ')
    result=int(line_split[0])
    values=tuple(int(value) for value in line_split[1].split(' '))
    parsed_line=(result,values)
    parsed_lines.add(parsed_line)
  return parsed_lines

def part_2(puzzle_input):
  return 0


def get_permutations(length):
  base = ['+', '*']
  return [list(p) for p in itertools.product(base, repeat=length)]

if __name__ == '__main__':
  main()
