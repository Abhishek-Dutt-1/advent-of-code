#%%
from pprint import pprint

f = open("input.txt", "r")
# f = open("input_2.txt", "r")
lines = f.readlines()
print(lines)
f.close()


#%%
for line in lines:
    row = line.replace("\n", "")
    print(row)


# %%
map = []
map_done = False
inst = None
max_len = 0
for line in lines:
    row = line.replace("\n", "")
    row = row.replace("\t", " ")
    # print(row)
    if not row:
        map_done = True

    if not map_done:
        map.append(row)
        max_len = max(max_len, len(row))
    else:
        inst = row

for ind, row in enumerate(map):
    map[ind] += " " * (max_len - len(row))

pprint(map)


# %%
def parse_inst(inst):
    parsed = []
    curr = ""
    for char in inst:
        if char.isnumeric():
            curr += char
        else:
            parsed.append(int(curr))
            curr = ""
            parsed.append(char)
    if curr:
        parsed.append(int(curr))
    return parsed


isnt_parsed = parse_inst(inst)
print(inst)
print(isnt_parsed)


# %%
# Find the top left coordinate
def find_top_left(map):
    for ind, row in enumerate(map):
        if row.replace(" ", ""):
            col = row.find(".")
            return (ind + 1, col + 1)


pos = find_top_left(map)


# %%
def get_first_dot(row):
    hash = row.find("#")
    dot = row.find(".")
    if hash == -1:
        return dot + 1
    if dot == -1:
        return hash + 1
    return min(dot, hash) + 1


pos = find_top_left(map)
print(pos)
# print(isnt_parsed)
dir = ">"
for ind, move in enumerate(isnt_parsed):
    # if ind == 9:
    #     break
    print(dir, move)
    if isinstance(move, int):
        match dir:
            case ">":
                row = map[pos[0] - 1]
                # print(row, len(row))
                # First dot or hash # 1 based index
                # first_dot = min(row.find("."), row.find("#")) + 1
                first_dot = get_first_dot(row)
                last_dot = max(row.rfind("."), row.rfind("#")) + 1
                # print(first_dot, last_dot, pos)
                curr_x = pos[1]  # 1 based index
                next_x = curr_x + 1
                if next_x > last_dot:
                    next_x = first_dot
                steps = 0
                while steps != move:
                    char = row[next_x - 1]
                    # print(steps, move, char, curr_x, next_x)
                    if char == ".":
                        steps += 1
                        curr_x = next_x
                        next_x += 1
                        if next_x > last_dot:
                            next_x = first_dot
                    if char == "#":
                        break
                    if char == " ":
                        next_x = first_dot
                pos = (pos[0], curr_x)
                # print(pos)
            case "D":
                row = "".join([row[pos[1] - 1] for row in map])
                # print(row, len(row))
                # First dot or hash # 1 based index
                # first_dot = min(row.find("."), row.find("#")) + 1
                first_dot = get_first_dot(row)
                last_dot = max(row.rfind("."), row.rfind("#")) + 1
                # print(first_dot, last_dot, pos)
                curr_y = pos[0]  # 1 based index
                next_y = curr_y + 1
                if next_y > last_dot:
                    next_y = first_dot
                steps = 0
                while steps != move:
                    char = row[next_y - 1]
                    # print(steps, move, char, curr_y, next_y)
                    if char == ".":
                        steps += 1
                        curr_y = next_y
                        next_y += 1
                        if next_y > last_dot:
                            next_y = first_dot
                    if char == "#":
                        break
                    if char == " ":
                        next_y = first_dot
                pos = (curr_y, pos[1])
                # print(pos)
            case "<":
                row = map[pos[0] - 1]
                # First dot or hash # 1 based index
                # first_dot = min(row.find("."), row.find("#")) + 1
                first_dot = get_first_dot(row)
                last_dot = max(row.rfind("."), row.rfind("#")) + 1
                curr_x = pos[1]  # 1 based index
                next_x = curr_x - 1
                steps = 0
                while steps != move:
                    char = row[next_x - 1]
                    if char == ".":
                        steps += 1
                        curr_x = next_x
                        next_x -= 1
                    if char == "#":
                        break
                    if char == " ":
                        next_x = last_dot
                pos = (pos[0], curr_x)
                # print(pos)
            case "^":
                row = "".join([row[pos[1] - 1] for row in map])
                # print(row)
                # First dot or hash # 1 based index
                # first_dot = min(row.find("."), row.find("#")) + 1
                first_dot = get_first_dot(row)
                last_dot = max(row.rfind("."), row.rfind("#")) + 1
                # print(first_dot, last_dot)
                curr_y = pos[0]  # 1 based index
                next_y = curr_y - 1
                steps = 0
                while steps != move:
                    char = row[next_y - 1]
                    # print(steps, move, char, curr_y, next_y)
                    if char == ".":
                        steps += 1
                        curr_y = next_y
                        next_y -= 1
                    if char == "#":
                        break
                    if char == " ":
                        next_y = last_dot
                pos = (curr_y, pos[1])
                # print(pos)

                pass

    if isinstance(move, str):
        match dir:
            case ">":
                if move == "L":
                    dir = "^"
                if move == "R":
                    dir = "D"
            case "D":
                if move == "L":
                    dir = ">"
                if move == "R":
                    dir = "<"
            case "<":
                if move == "L":
                    dir = "D"
                if move == "R":
                    dir = "^"
            case "^":
                if move == "L":
                    dir = "<"
                if move == "R":
                    dir = ">"

print(pos)
print(1000 * pos[0] + 4 * pos[1] + {">": 0, "D": 1, "<": 2, "^": 3}[dir])

# %%
print(map)


# %%
import pandas as pd
df = pd.DataFrame([list(row) for row in map])
df.to_csv("tmp.csv")


# %%
