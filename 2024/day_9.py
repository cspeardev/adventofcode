#!/usr/bin/env python3
'''Day 9 of Advent of Code'''
import utilities
import time

def part_1(input_file_content:str):
  blocks = parse_blocks(input_file_content)
  while(find_last_data_block_index(blocks) != (find_first_empty_index(blocks)-1)):
    swap_indexes(blocks,
                 find_first_empty_index(blocks),
                 find_last_data_block_index(blocks))
  checksum = get_blocks_checksum(blocks)
  return checksum

def part_2(input_file_content:str):
  blocks = parse_blocks(input_file_content)
  files=parse_files_from_blocks(blocks)
  for file_content,file_indexes in reversed(files.items()):
    file_size=len(file_indexes)
    start = find_empty_span(blocks,file_size)
    if start != -1 and all(start < file_index for file_index in file_indexes):
      target_indexes=[]
      for i in range(file_size):
        target_indexes.append(start+i)
      swap_index_range(blocks,file_indexes,target_indexes)
  return get_blocks_checksum(blocks)

def parse_files_from_blocks(blocks):
  file_indexes_dictionary={}
  for block_index,block in enumerate(blocks):
    if block > -1:
      if not block in file_indexes_dictionary.keys():
        file_indexes_dictionary[block]=[]
      file_indexes_dictionary[block].append(block_index)
  return file_indexes_dictionary

def find_empty_span(blocks,size):
  length=1
  for i, value in enumerate(blocks):
    if isinstance(value, int) and value == -1:
      start = i
      while i+1 < len(blocks) and blocks[i+1]==-1:  # Find the end of the current span by checking next values
        i += 1
      length = i - start + 1
      if length >= size:
        return start
  return -1

def get_file_block_indexes(blocks,file_start_index):
  file_indexes = []
  value = blocks[file_start_index]
  reversed_start_index = len(blocks)-1-file_start_index
  blocks_reversed = blocks.copy()
  blocks_reversed.reverse()
  length = 1
  for block in blocks_reversed[reversed_start_index+1:]:
    if block == value:
      length += 1
  for i in range(length):
    file_indexes.append(file_start_index-i)
  return file_indexes


def parse_blocks(input_file_content):
  blocks=[]
  block_id = 0
  for i,block_value in enumerate(input_file_content):
    num=int(block_value)
    if(i%2):
      for _ in range(num):
        blocks.append(-1)
    else:
      for _ in range(num):
        blocks.append(block_id)
      block_id+=1
  return blocks

def find_first_empty_index(blocks:list):
  if blocks is None:
    blocks = []
  return blocks.index(-1)

def find_last_data_block_index(blocks:list):
  blocks_reversed = blocks.copy()
  blocks_reversed.reverse()
  for i,value in enumerate(blocks_reversed):
    if value > -1:
      test = len(blocks) - 1 - i
      return test

def get_blocks_checksum(blocks:list):
  checksum = 0
  for i,block in enumerate(blocks):
    if block != -1:
      checksum += block*i
    else:
      continue
  return checksum

def swap_indexes(blocks:list,
                 x:int,
                 y:int):
  blocks[x], blocks[y] = blocks[y], blocks[x]

def swap_index_range(blocks:list,
                       x:[int],
                       y:[int]):
  for i in range(len(x)):
    swap_indexes(blocks,x[i],y[i])


def main():
  input_file_content = utilities.get_input_file_content()

  # part_1_start_time = time.time()
  # part_1_solution=part_1(input_file_content)
  # part_1_end_time = time.time()

  # print(f'Solution for part 1: {part_1_solution}')
  # part_1_elapsed_time = part_1_end_time - part_1_start_time
  # print(f'Elapsed time for part 1: {str(part_1_elapsed_time*1000)}')

  part_2_start_time = time.time()
  part_2_solution=part_2(input_file_content)
  part_2_end_time = time.time()

  print(f'Solution for part 2: {part_2_solution}')
  part_2_elapsed_time = part_2_end_time - part_2_start_time
  print(f'Elapsed time for part 2: {str(part_2_elapsed_time*1000)}')

if __name__ == '__main__':
  main()

