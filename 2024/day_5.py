#!/usr/bin/env python3
'''Day 5 of Advent of Code'''
import time
import utilities

def sum_middle_values(sets):
  return sum([page_set[int(len(page_set)/2)] for page_set in sets])

def part_1(input_file_content:str):
  lines = input_file_content.splitlines()
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
  return sum_middle_values(valid_page_sets)

def part_2(input_file_content:str):
  lines = input_file_content.splitlines()
  blank_line_index = next(i for i, x in enumerate(lines) if not x.strip())
  rules_lines = {x.strip() for x in lines[:blank_line_index]}
  pages_lines = {x.strip() for x in lines[blank_line_index+1:]}
  corrected_page_sets = []
  rules = [tuple(int(value) for value in line.split('|'))
        for line in rules_lines]
  pages_sets=[list(int(value) for value in line.split(','))
              for line in pages_lines]
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
  return sum_middle_values(corrected_page_sets)

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
