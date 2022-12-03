#%%
with open('input.txt') as input_file:
    rucksacks = []
    for line in input_file:
        line = line.strip()
        rucksacks.append(line)
      

#%%
def total_priority(item_list):
    '''Returns the sum of priorities from a list of item codes.'''
    total = 0

    for item in item_list:
        char_num = ord(item)
        item_priority = 0

        if str.islower(item):
            priority = char_num - 96
        elif str.isupper(item):
            priority = char_num - 38

        total += priority
    
    return total


def part_one():
    rucksack_overlap = []
    for rucksack in rucksacks:
        compartment_size = int(len(rucksack)/2)
        compartment1 = set(rucksack[:compartment_size])
        compartment2 = set(rucksack[compartment_size:])
        overlap_item = compartment1.intersection(compartment2).pop()
        rucksack_overlap.append(overlap_item)
          
    return total_priority(rucksack_overlap)

def part_two():
    group_starts = range(0, len(rucksacks), 3) # list of points where groups start in input
    
    # list of grouped rucksacks
    groups = []
    for start in group_starts:
        group = rucksacks[start:start+3]
        groups.append(group)

    # list of badge types from grouped rucksacks
    group_badges = []
    for group in groups:
        group = [set(rucksack) for rucksack in group]
        badge = group[0] & group[1] & group[2]
        group_badges.append(badge.pop())
    
    return total_priority(group_badges)


if __name__ == '__main__':
    print(part_one())
    print(part_two())

    


# %%
