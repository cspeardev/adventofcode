#!/usr/bin/env python3
'''Day five of Advent of Code'''
import time
import os

def sum_middle_values(sets):
  return sum([page_set[int(len(page_set)/2)] for page_set in sets])

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

# Assume that any pages only occur once in each set

for pages in pages_sets:
  is_page_set_valid = True
  applicable_rules_for_page_set = []
  for rule in rules:
    if all(element in pages for element in rule):
      applicable_rules_for_page_set.append(rule)
  for page_index,page in enumerate(pages):
    applicable_rules_for_page = [rule for rule
                                 in applicable_rules_for_page_set
                                 if rule[0] == page]
    for rule in applicable_rules_for_page:
      occurence_index = pages.index(rule[1])
      if occurence_index < page_index:
        is_page_set_valid = False
        break

  if is_page_set_valid:
    valid_page_sets.append(pages)



solution = sum_middle_values(valid_page_sets)

print(f"Solution for part 1 is {solution}")

end_time = time.time()
elapsed_time = end_time - start_time
elapsed_time_in_milliseconds = elapsed_time * 1000
print('Elapsed time for part 2: ' + str(elapsed_time_in_milliseconds))

# --- Part 2
start_time = time.time()
corrected_page_sets = []

for pages in pages_sets:
  add_this_set = False
  is_page_set_valid = True
  applicable_rules_for_page_set = []
  for rule in rules:
    if all(element in pages for element in rule):
      applicable_rules_for_page_set.append(rule)
  for page_index,page in enumerate(pages):
    applicable_rules_for_page = [rule for rule
                                 in applicable_rules_for_page_set
                                 if rule[0] == page]
    for before,after in applicable_rules_for_page:
      after_index = pages.index(after)
      before_index = pages.index(before)
      if after_index < before_index:
        add_this_set = True
        value = pages.pop(before_index)
        pages.insert(after_index,value)
  if add_this_set:
    corrected_page_sets.append(pages)


solution = sum_middle_values(corrected_page_sets)
print(f"Solution for part 2 is {solution}")

end_time = time.time()
elapsed_time = end_time - start_time
elapsed_time_in_milliseconds = elapsed_time * 1000
print('Elapsed time for part 2: ' + str(elapsed_time_in_milliseconds))
