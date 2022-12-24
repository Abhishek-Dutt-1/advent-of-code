#%%
from pprint import pprint
import copy

# f = open("input_2.txt", "r")
f = open("input.txt", "r")
lines = f.readlines()
print(lines)
f.close()


# %%
def get_adjecent_cubes(row):
    neighbours = []
    for delta in [-1, 1]:
        neighbours.append((row[0] + delta, row[1], row[2]))
        neighbours.append((row[0], row[1] + delta, row[2]))
        neighbours.append((row[0], row[1], row[2] + delta))

    return neighbours

seen = set()
blocked = 0
blocks_count = 0
for line in lines:
    row = line.replace("\n", "")
    row = row.split(",")
    row = map(int, row)
    row = tuple(row)
    # print(row)
    seen.add(row)
    blocks_count += 1
    neighbours = get_adjecent_cubes(row)
    # print(neighbours)
    for neigh in neighbours:
        if neigh in seen:
            blocked += 1


op = (blocks_count * 6) - (2*blocked)
print(op)


# 6 = 6
# 10 = 6 + 6 - 2*1
# 14 = 6 + 6 + 6 -2*2
# 16 = 6 + 6 + 6 + 6 - 2*4
# 20 = 5*6 - 2*5

# %%
