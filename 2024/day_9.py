#!/usr/bin/env python3
'''Day 9 of Advent of Code'''
import utilities
import time
import numpy as np

def part_1(input_file_content:str):
  blocks = parse_blocks(input_file_content)
  empty_indexes=find_empty_block_indexes(blocks)
  populated_indexes=find_populated_block_indexes(blocks)
  for i,block_index in enumerate(reversed(populated_indexes)):
    if i < len(empty_indexes) and empty_indexes[i] < block_index:
      swap_indexes(blocks,block_index,empty_indexes[i])
    else:
      break
  checksum = get_blocks_checksum(blocks)
  return checksum

def part_2(input_file_content:str):
  blocks = parse_blocks(input_file_content)
  files=parse_files_from_blocks(blocks)
  empty_spans=find_empty_spans(blocks)
  for file_indexes in reversed(files.values()):
    file_size=len(file_indexes)
    target_span_index=find_empty_span_of_size(empty_spans,file_size)
    if target_span_index != -1:
      start=empty_spans[target_span_index][0]
      if start != -1 and all(start < file_index for file_index in file_indexes):
        target_indexes=[]
        for i in range(file_size):
          target_indexes.append(start+i)
        swap_index_range(blocks,file_indexes,target_indexes)
      if len(empty_spans[target_span_index]) == file_size:
        empty_spans.pop(target_span_index)
      else:
        empty_spans[target_span_index] = empty_spans[target_span_index][file_size:]
  return get_blocks_checksum(blocks)

def find_empty_span_of_size(blocks,size):
  for i, lst in enumerate(blocks):
    if len(lst) >= size:
      return i
  return -1

def parse_files_from_blocks(blocks):
  file_indexes_dictionary={}
  for block_index,block in enumerate(blocks):
    if block > -1:
      if not block in file_indexes_dictionary:
        file_indexes_dictionary[block]=[]
      file_indexes_dictionary[block].append(block_index)
  return file_indexes_dictionary

def find_empty_spans(blocks):
  empty_indexes=find_empty_block_indexes(blocks)
  result=[]
  temp = [empty_indexes[0]]
  for i in range(1, len(empty_indexes)):
    if empty_indexes[i] == empty_indexes[i-1]+1:
      temp.append(empty_indexes[i])
    else:
      result.append(temp[:])
      temp = [empty_indexes[i]]
  result.append(temp)
  return result

def parse_blocks(input_file_content):
  blocks=[]
  block_id = 0
  for i,block_value in enumerate(input_file_content):
    num=int(block_value)
    if i%2:
      for _ in range(num):
        blocks.append(-1)
    else:
      for _ in range(num):
        blocks.append(block_id)
      block_id+=1
  return blocks

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
                       x:list[int],
                       y:list[int]):
  for i in range(len(x)):
    swap_indexes(blocks,x[i],y[i])

def find_empty_block_indexes(lst):
  return np.where(np.array(lst) == - 1)[0]

def find_populated_block_indexes(lst):
  return np.where(np.array(lst) > - 1)[0]

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

