#!/usr/bin/env python3
'''Day five of Advent of Code'''
import time
import os

# --- Part One

start_time = time.time()

script_dir = os.path.dirname(__file__)
input_file_path = script_dir + '/input/5'

with open(input_file_path,encoding='utf-8') as input_file:
  lines = [line.strip() for line in input_file]

blank_line_index = next(i for i, x in enumerate(lines) if not x.strip())

rules_lines = {x.strip() for x in lines[:blank_line_index]}

pages_lines = {x.strip() for x in lines[blank_line_index+1:]}

rules = [tuple(int(value) for value in line.split('|'))
         for line in rules_lines]
pages_sets=[list(int(value) for value in line.split(','))
            for line in pages_lines]

valid_page_sets=[]

for pages in pages_sets:
  is_page_set_valid = True
  applicable_rules_for_page_set = []
  for rule in rules:
    if all(element in pages for element in rule):
      applicable_rules_for_page_set.append(rule)
  for i,page in enumerate(pages):
    applicable_rules_for_page = [rule for rule
                                 in applicable_rules_for_page_set
                                 if rule[0] == page]
    for rule in applicable_rules_for_page:
      occurence_indexes = [index for index,value
                           in enumerate(pages) if value == rule[1]]
      if any(index < i for index in occurence_indexes):
        is_page_set_valid = False
        break
  if is_page_set_valid:
    valid_page_sets.append(pages)

solution = sum([page_set[int(len(page_set)/2)] for page_set in valid_page_sets])

print(f"Solution for part 1 is {solution}")

end_time = time.time()
elapsed_time = end_time - start_time
elapsed_time_in_milliseconds = elapsed_time * 1000
print('Elapsed time for part one: ' + str(elapsed_time_in_milliseconds))