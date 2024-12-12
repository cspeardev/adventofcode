#!/usr/bin/env python3
'''Day 9 of Advent of Code'''
from collections import deque
from itertools import chain
import math

import numpy
import utilities
import time
import asyncio

def part_1(input_file_content:str):
  stones=deque([int(stone) for stone in input_file_content.split(' ')])
  for _ in range(25):
    stones=asyncio.run(blink(stones))
  return len(stones)

def part_2(input_file_content:str):
  stones=deque([int(stone) for stone in input_file_content.split(' ')])
  for _ in range(75):
    stones=asyncio.run(blink(stones))
  return len(stones)

async def blink(stones:tuple[int])->tuple[int]:
  tasks = [asyncio.create_task(transform_stone(stone)) for stone in stones]
  results = await asyncio.gather(*tasks)
  blinked_stones = tuple(chain.from_iterable(results))
  return blinked_stones

async def transform_stone(stone:int)->tuple[int]:
  if stone == 0:
    return (1,)
  else:
    stone_str=str(stone)
    stone_str_len=len(stone_str)
    if stone_str_len%2==0:
      midpoint = stone_str_len // 2
      return(int(stone_str[:midpoint]), int(stone_str[midpoint:]))
    else:
      return(stone*2024,)

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

