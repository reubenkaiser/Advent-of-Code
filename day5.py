#%%
import numpy as np
import re
from AoC import AoC
session = AoC()

#%%
with open('inputs/input5.txt') as input_file:
    contents = input_file.readlines()
    contents = [line.rstrip() for line in contents]

# Split the input into the structure and instruction components
split_idx = contents.index('')    
structure_raw = contents[:split_idx]
instructions = contents[split_idx + 1:]

def build_stack(structure_raw):
    structure = structure_raw.copy()

    # Processing structure into list of lists for each stack
    index_line = list(structure.pop())
    block_indexes = []

    for idx, character in enumerate(index_line):
        if character != ' ':
            block_indexes.append(idx)

    structure.reverse() # reverse to build stacks from bottom up
    stack_list = []
    for idx in block_indexes:
        stack = [line[idx] for line in structure if line[idx] != ' ']
        stack_list.append(stack)
    
    return stack_list

def part_one():
    stack = build_stack(structure_raw)

    # Processing instructions into manipulations
    def perform_task(task_string):
        task = re.findall(
            pattern='move ([0-9]*) from ([0-9]*) to ([0-9]*)'
            , string=task_string
        ).pop()

        num = int(task[0])
        from_idx = int(task[1]) - 1
        to_idx = int(task[2]) - 1

        for i in range(0, num):
            stack[to_idx].append(stack[from_idx].pop())

    for task in instructions:
        perform_task(task)

    return ''.join([stack.pop() for stack in stack])

def part_two():
    stack = build_stack(structure_raw)

    # Processing instructions into manipulations
    def perform_task(task_string):
        task = re.findall(
            pattern='move ([0-9]*) from ([0-9]*) to ([0-9]*)'
            , string=task_string
        ).pop()

        num = int(task[0])
        from_idx = int(task[1]) - 1
        to_idx = int(task[2]) - 1
        
        lifted = stack[from_idx][-num:] # crates lifted in task
        stack[from_idx] = stack[from_idx][:-num] # stack after lifting
        stack[to_idx].extend(lifted) # stack after dropping
    
    for task in instructions:
        perform_task(task)

    return ''.join([stack.pop() for stack in stack])

if __name__ == '__main__':
    print(part_one())
    print(part_two())