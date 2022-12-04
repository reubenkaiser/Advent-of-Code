#%%
import numpy as np
from AoC import AoC

session = AoC()

#%% Part 1

inventories = []
with open('inputs/input1.txt') as input_file:
    inventory = []
    for line in input_file:
        if line != '\n':
            inventory.append(int(line))
        elif line == '\n':
            inventories.append(inventory)
            inventory = []

totals = [sum(inventory) for inventory in inventories]

max_elf = np.argmax(totals)
totals[max_elf]


# %% Part 2
def top_n_elves(n, totals):
    totals_c = totals.copy()
    cal_total = 0
    for i in range(0, n):
        max_elf = np.argmax(totals_c)
        max_cal = totals_c.pop(max_elf)
        cal_total += max_cal

        print(f'{i+1}: Elf {max_elf+1} has {max_cal} Calories')

    print(f'Combined Calories: {cal_total}')

top_n_elves(3, totals)
# %%
