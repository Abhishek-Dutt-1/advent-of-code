#%%
f = open("input.txt", "r")
lines = f.readlines()
print(lines)
f.close()


#%%
class node:
    def __init__(self, name, type, size, parent):
        self.type = type
        self.size = size
        self.name = name
        self.children = []
        self.parent = parent
        self.sub_size = 0

    def search_child(self, name):
        child = [child for child in self.children if child.name == name]
        if child:
            return child[0]
        else:
            return None

    def to_string(self, ind = 0):
        text = "\t"*ind + self.name + " " + self.type + " " + str(self.size) + " " + str(self.sub_size) + "\n"
        for child in self.children:
            text += child.to_string(ind+1)
        return text

#%%
root = node("/", "dir", 0, None)
curr = None
ls_flag = False
for line in lines:
    row = line.replace("\n", "")
    if ls_flag:
        row_arr = row.split()
        if row_arr[0].isnumeric():
            curr.children.append(node(row_arr[1], "file", int(row_arr[0]), curr))
            curr.sub_size += int(row_arr[0])
        elif row_arr[0] != "$":
            curr.children.append(node(row_arr[1], "dir", 0, curr))

    if row[0] == "$":
        ls_flag = False
        cmd = row.split()
        if cmd[1] == "cd":
            dir = cmd[2]
            if dir == "/":
                curr = root
            elif dir == "..":
                curr = curr.parent
            else:
                child = curr.search_child(dir)
                assert child is not None
                curr = child
                
        if cmd[1] == "ls":
            ls_flag = True

    print(row)


# %%
print(root.to_string(0))


# %%
def travese(n):
    if n.type == "file":
        return n.size
    size = 0
    for child in n.children:
        size += travese(child)
    if size <= 100000:
        # print(size, n.name)
        print(size)
    return size


#%%
travese(root)

# %%
def travese(n):
    if n.type == "file":
        return n.size
    size = 0
    for child in n.children:
        size += travese(child)
    if size >= 6090134:
        # print(size, n.name)
        print(size, n.name)
    return size


#%%
travese(root)


# %%
