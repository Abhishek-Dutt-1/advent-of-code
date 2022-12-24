#%%
from pprint import pprint

# f = open("input_2.txt", "r")
f = open("input.txt", "r")
lines = f.readlines()
print(lines)
f.close()


#%%
for line in lines:
    row = line.replace("\n", "")
    print(row)


# %%
def connect(start, end, grid):
    # print("=", start, end)
    assert start[0] == end[0] or start[1] == end[1]
    if start[0] == end[0]:
        if start[1] > end[1]:
            tmp = end
            end = start
            start = tmp
        for y in range(start[1], end[1] + 1):
            grid[y][start[0] - min_x] = "#"
    if start[1] == end[1]:
        if start[0] > end[0]:
            tmp = end
            end = start
            start = tmp
        for x in range(start[0], end[0] + 1):
            grid[start[1]][x - min_x] = "#"


# Test case:
# (494, 4), (503, 9)
# Whole data:
# (490, 14), (573, 182)
min_x = 494
max_x = 503 - 494 + 1
max_y = 9 - 0 + 1

min_x = 490
max_x = 573 - 490 + 1
max_y = 182 - 0 + 1
grid = [["."] * max_x for _ in range(max_y)]

for line in lines:
    row = line.replace("\n", "")
    print(row)
    coords = row.split(" -> ")
    for ind in range(len(coords) - 1):
        start = coords[ind].split(",")
        start = tuple(map(int, start))
        end = coords[ind + 1].split(",")
        end = tuple(map(int, end))
        connect(start, end, grid)

grid[0][500 - min_x] = "+"

# %%
pprint(grid)

# %%
def check_oob(i, j):
    if i < 0 or i >= max_y or j < 0 or j >= max_x:
        print(i < 0, i >= max_y, j < 0, j >= max_x)
        print("OOB:", i, j)
        return True
    return False


i, j = 0, 500 - min_x

drop_oob = False
drops = 0
while not drop_oob:
    # print("NEW DROP")
    drops += 1
    print("NEW DROP", drops)
    i, j = 0, 500 - min_x
    drop_rest = False
    while not drop_rest and not drop_oob:
        # print(i, j)
        if check_oob(i + 1, j):
            grid[i][j] = drops
            print("DOWN")
            drop_oob = True
        elif grid[i + 1][j] == ".":
            i += 1
        elif check_oob(i + 1, j - 1):
            grid[i][j] = drops
            print("LEFT")
            drop_oob = True
        elif grid[i + 1][j - 1] == ".":
            i += 1
            j -= 1
        elif check_oob(i + 1, j + 1):
            print("RIGHT")
            grid[i][j] = drops
            drop_oob = True
        elif grid[i + 1][j + 1] == ".":
            i += 1
            j += 1
        else:
            # grid[i][j] = "o"
            grid[i][j] = drops
            drop_rest = True
            # pprint(grid)

print("LAST DROP", drops)


# %%
print(drops - 1)

# %%
import pandas as pd
import csv

df = pd.DataFrame(grid)
df.to_csv("tmp.csv")

with open("new_file.csv", "w") as my_csv:
    csvWriter = csv.writer(my_csv, delimiter=",")
    csvWriter.writerows(grid)


# %%

# PART 2 ###########################################################

# Test case:
# (494, 4), (503, 9)

# Whole data:
# (490, 14), (573, 182)

from pprint import pprint

# f = open("input_2.txt", "r")
f = open("input.txt", "r")
lines = f.readlines()
print(lines)
f.close()


# %%
def connect(start, end, grid):
    # print("=", start, end)
    assert start[0] == end[0] or start[1] == end[1]
    if start[0] == end[0]:
        if start[1] > end[1]:
            tmp = end
            end = start
            start = tmp
        for y in range(start[1], end[1] + 1):
            grid[y][start[0] - min_x] = "#"
    if start[1] == end[1]:
        if start[0] > end[0]:
            tmp = end
            end = start
            start = tmp
        for x in range(start[0], end[0] + 1):
            grid[start[1]][x - min_x] = "#"


# Test case:
# (494, 4), (503, 9)
min_x = 494 - 200
max_x = 503 - 494 + 1 + 200 + 200
max_y = 9 - 0 + 1

# Whole data:
# (490, 14), (573, 182)
offset = 2000
min_x = 490 - offset
max_x = 573 - 490 + 1 + (2*offset)
max_y = 182 - 0 + 1
grid = [["."] * max_x for _ in range(max_y)]
print("=", max_x, min_x, (max_x - min_x), len(grid), len(grid[0]))

for line in lines:
    row = line.replace("\n", "")
    print(row)
    coords = row.split(" -> ")
    for ind in range(len(coords) - 1):
        start = coords[ind].split(",")
        start = tuple(map(int, start))
        end = coords[ind + 1].split(",")
        end = tuple(map(int, end))
        connect(start, end, grid)

grid[0][500 - min_x] = "+"

# %%
pprint(grid)


# %%
# Add FLOOR
grid.append(["."] * max_x)
grid.append(["#"] * max_x)
max_y = max_y + 2

# %%
pprint(grid)

# %%
def check_oob(i, j):
    if i < 0 or i >= max_y or j < 0 or j >= max_x:
        print(i < 0, i >= max_y, j < 0, j >= max_x)
        print("OOB:", i, j)
        return True
    return False


i, j = 0, 500 - min_x

drop_oob = False
drops = 0
blocked = False
while not drop_oob and not blocked:
    # print("NEW DROP")
    drops += 1
    print("NEW DROP", drops)
    i, j = 0, 500 - min_x
    drop_rest = False
    while not drop_rest and not drop_oob:
        # print(i, j)
        if check_oob(i + 1, j):
            grid[i][j] = drops
            print("DOWN")
            drop_oob = True
        elif grid[i + 1][j] == ".":
            i += 1
        elif check_oob(i + 1, j - 1):
            grid[i][j] = drops
            print("LEFT")
            drop_oob = True
        elif grid[i + 1][j - 1] == ".":
            i += 1
            j -= 1
        elif check_oob(i + 1, j + 1):
            print("RIGHT")
            grid[i][j] = drops
            drop_oob = True
        elif grid[i + 1][j + 1] == ".":
            i += 1
            j += 1
        else:
            # grid[i][j] = "o"
            if i == 0 and j == 500 - min_x:
                print("BLOCKED")
                blocked = True
                break
            grid[i][j] = drops
            drop_rest = True
            # pprint(grid)

print("LAST DROP", drops)


# %%
import pandas as pd

df = pd.DataFrame(grid)
df.to_csv("tmp.csv")


# %%
