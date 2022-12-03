#%%
with open('input.txt') as input_file:
    rucksacks = []
    for line in input_file:
        line = line.strip()
        rucksacks.append(line)
      

#%%
def part_one():
    rucksack_overlap = []
    for rucksack in rucksacks:
        compartment_size = int(len(rucksack)/2)
        compartment1 = set(rucksack[:compartment_size])
        compartment2 = set(rucksack[compartment_size:])
        overlap_item = compartment1.intersection(compartment2).pop()
        rucksack_overlap.append(overlap_item)

    total_priority = 0

    for item in rucksack_overlap:
        char_num = ord(item)
        item_priority = 0

        if str.islower(item):
            priority = char_num - 96
        elif str.isupper(item):
            priority = char_num - 38

        total_priority += priority    
        
    return total_priority

if __name__ == '__main__':
    print(part_one())

# %%
