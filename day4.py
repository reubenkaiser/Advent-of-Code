#%%
from AoC import AoC
session = AoC()

# load data as a list of paired ranges
with open('inputs/input4.txt') as input_file:
    paired_elf_duties = []
    for line in input_file:
        line = line.strip()
        pair = line.split(',')
        pair = [id_range.split('-') for id_range in pair]
        pair = [
            set(
                range(
                    int(id_range[0])
                    , int(id_range[1]) + 1
                )
            ) for id_range in pair
        ]
        paired_elf_duties.append(pair)

#%%
def part_one():
    count = 0
    for pair in paired_elf_duties:
        elf_one = pair[0]
        elf_two = pair[1]

        if elf_one.issubset(elf_two) or elf_one.issuperset(elf_two):
            count += 1

    return count


def part_two():
    count = 0
    for pair in paired_elf_duties:
        elf_one = pair[0]
        elf_two = pair[1]

        if not elf_one.isdisjoint(elf_two):
            count += 1
    
    return count


if __name__ == '__main__':
    print(part_one())
    print(part_two())

