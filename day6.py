#%%
from AoC import AoC
session = AoC()

# %%
with open('inputs/input6.txt') as input_file:
    stream = input_file.readline().strip()

# %%
def process_stream(stream, offset):
    for start in range(0, len(stream) - offset):
        window = stream[start:start + offset]
        if len(set(window)) == offset:
            return start + offset

if __name__ == '__main__':
    print(process_stream(stream, 4))
    print(process_stream(stream, 14))
