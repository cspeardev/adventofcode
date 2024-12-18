#!/usr/bin/env python3
'''Day 17 of Advent of Code'''
import re
from typing import Dict
import utilities
import time

def load_registers(input_file_content,letter):
  register_regex=r'Register {}: (\d*)$'
  register = re.findall(register_regex.format(letter),
                        input_file_content,
                        re.M)[0]
  return int(register)

def load_program(input_file_contnet):
  program_regex=r'Program: (.*)$'
  program_content=re.findall(program_regex,input_file_contnet,re.M)[0]
  program_values=tuple(int(value) for value in program_content.split(','))
  return program_values

def get_combo_operand(registers:Dict[str,int],
                      value:int):
  if 0 <= value <= 3:
    return value
  if value == 4:
    return registers['A']
  if value == 5:
    return registers['B']
  if value == 6:
    return registers['C']

def adv(registers:Dict[str,int],operand:int):
  numerator=registers['A']
  denominator=2**get_combo_operand(registers,operand)
  product=numerator/denominator
  registers['A']=int(product)

def bxl(registers:Dict[str,int],operand:int):
  registers['B'] = registers['B'] ^ operand

def bst(registers:Dict[str,int],operand:int):
  registers['B']=get_combo_operand(registers,operand)%8

#Assign to instruction pointer
def jnz(registers:Dict[str,int],operand:int):
  if registers['A'] != 0:
    return operand

def out(registers:Dict[str,int],operand:int):
  return get_combo_operand(registers,operand) % 8

#Add return to outputs
def bxc(registers:Dict[str,int]):
  registers['B'] = registers['B'] ^ registers['C']

def bdv(registers:Dict[str,int],operand:int):
  numerator=registers['A']
  denominator=2**get_combo_operand(registers,operand)
  product=numerator/denominator
  registers['B']=int(product)

def cdv(registers:Dict[str,int],operand:int):
  numerator=registers['A']
  denominator=2**get_combo_operand(registers,operand)
  product=numerator/denominator
  registers['C']=int(product)

def part_1(input_file_content:str):
  instruction_pointer=0
  registers={}
  registers['A']=load_registers(input_file_content,'A')
  registers['B']=load_registers(input_file_content,'B')
  registers['C']=load_registers(input_file_content,'C')
  program = load_program(input_file_content)
  output = []
  while 0 <= instruction_pointer <= len(program)-1:
    opcode=program[instruction_pointer]
    operand=program[instruction_pointer+1]
    match opcode:
      case 0:
        adv(registers,operand)
      case 1:
        bxl(registers,operand)
      case 2:
        bst(registers,operand)
      case 3:
        jumped_instruction_pointer=jnz(registers,operand)
        if jumped_instruction_pointer is not None:
          instruction_pointer=jumped_instruction_pointer
          continue
      case 4:
        bxc(registers)
      case 5:
        output.append(out(registers,operand))
      case 6:
        bdv(registers,operand)
      case 7:
        cdv(registers,operand)
    instruction_pointer+=2
  return ','.join(str(val) for val in output)

def part_2(input_file_content:str):
  return 0

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
