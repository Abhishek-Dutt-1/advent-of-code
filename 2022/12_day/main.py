#%%
# f = open("input.txt", "r")
f = open("input_2.txt", "r")
lines = f.readlines()
print(lines)
f.close()


#%%
for line in lines:
    row = line.replace("\n", "")
    print(row)


#%%
data = []
for line in lines:
    row = line.replace("\n", "")
    data.append(list(row))


class node:
    def __init__(self, name):
        self.name = name
        self.children = []


#%%
root = None
curr = None
rows = len(data)
cols = len(data[0])

def is_safe(data, curr, next):
    pass

def tree(data, start):
    q = []
    seen = set()
    q.append(start)
    seen.add(start)
    while q:
        curr = q.pop(0)


        for next in [
            (curr[0], curr[1] + 1),
            (curr[0], curr[1] - 1),
            (curr[0] + 1, curr[1]),
            (curr[0] - 1, curr[1]),
        ]:
            if is_safe(data, curr, next) and next not in seen:
                q.append(next)
                seen.add(next)


tree(data, (0, 0))


#%%
