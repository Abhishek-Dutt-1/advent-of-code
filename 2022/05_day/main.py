#%%
f = open("input_2.txt", "r")
lines = f.readlines()
print(lines)
f.close()


#%%
for line in lines:
    row = line.replace("\n", "")
    print(row)


#%%
stacks = [
    ["N", "V", "C", "S"],
    ["S", "N", "H", "J", "M", "Z"],
    ["D", "N", "J", "G", "T", "C", "M"],
    ["M", "R", "W", "J", "F", "D", "T"],
    ["H", "F", "P"],
    ["J", "H", "Z", "T", "C"],
    ["Z", "L", "S", "F", "Q", "R", "P", "D"],
    ["W", "P", "F", "D", "H", "L", "S", "C"],
    ["Z", "G", "N", "F", "P", "M", "S", "D"],
]


#%%
stacks2 = []
for stack in stacks:
    stacks2.append(list(reversed(stack)))


# %%
for line in lines:
    row = line.replace("\n", "")
    print(row)
    _, num, _, dest, _, target = row.split()
    num = int(num)
    dest = int(dest) - 1
    target = int(target) - 1
    print(num, dest, target)
    for n in range(num):
        stacks2[target].append(stacks2[dest].pop())


# %%
for stack in stacks2:
    print(stack)

# %%
JCGSQRCFJ < --Wrong
SZMTPCDCD < --Wrong
CNSZFDVLJ < --Correct

#%%
for line in lines:
    row = line.replace("\n", "")
    print(row)
    _, num, _, dest, _, target = row.split()
    num = int(num)
    dest = int(dest) - 1
    target = int(target) - 1
    print(num, dest, target)
    l = len(stacks2[dest])
    temp = stacks2[dest][(l - num) :]
    stacks2[dest] = stacks2[dest][: l - num]
    stacks2[target] += temp


# %%
QNDWLMGNS < --Correct
