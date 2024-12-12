#!/usr/bin/env python3
'''Day 9 of Advent of Code'''
import utilities
import time
def part_1(input_file_content:str):
  return process_stones(input_file_content,25)

def part_2(input_file_content:str):
  return process_stones(input_file_content,75)

def process_stones(input_file_content,count):
  stones=[(int(stone),1) for stone in input_file_content.split(' ')]
  stones=consolidate_stones(stones)
  for _ in range(count):
    stones=blink(stones)
  solution=sum(count for _,count in stones)
  return solution

def consolidate_stones(tuples:list[tuple[int]]):
  tuples.sort()
  consolidated_dict = {}
  for t in tuples:
    if t[0] not in consolidated_dict:
      consolidated_dict[t[0]] = t[1]
    else:
      consolidated_dict[t[0]] += t[1]
  consolidated_tuples = [(k, v) for k, v in consolidated_dict.items()]
  return consolidated_tuples

def blink(stones:list[tuple[int]])->list[tuple[int]]:
  stones = consolidate_stones(stones)
  blinked_stones=[()]*0
  for stone_value,stone_count in stones:
    if stone_value==0:
      blinked_stones.append((1,stone_count))
      continue
    stone_str = str(stone_value)
    stone_str_len = len(stone_str)
    if stone_str_len%2==0:
      midpoint = stone_str_len // 2
      blinked_stones.append((int(stone_str[:midpoint]),stone_count))
      blinked_stones.append((int(stone_str[midpoint:]),stone_count))
      continue
    blinked_stones.append((stone_value*2024,stone_count))
  return blinked_stones

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

