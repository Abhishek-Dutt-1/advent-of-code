#%%
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
def split_by_op(op_str):
    op_list = [" + ", " - ", " * ", " / "]
    for ops in op_list:
        split = op_str.split(ops)
        if len(split) == 2:
            left = split[0]
            right = split[1]
            op = ops.strip()
            return left, right, op

class node:
    def __init__(self, name, val=None, op=None):
        self.name = name
        self.val = val
        self.op = op
        self.left = None
        self.right = None

    def __str__(self):
        return f"{self.name}, {self.val}, {self.op}"

    def print_tree(self, level=0):
        s = "\t" * level + f"{self}\n"
        for child in [self.left, self.right]:
            if child:
                s += child.print_tree(level + 1)
        return s

# Create cache from nodes
cache = {}
for line in lines:
    row = line.replace("\n", "")
    print(row)
    name, op = row.split(":")
    op = op.strip()
    if op.isnumeric():
        if name in cache:
            cache[name].val = int(op)
        else:
            cache[name] = node(name, val=int(op))
    else:
        left, right, op = split_by_op(op)

        curr = None
        if name in cache:
            curr = cache[name]
            curr.op = op
        else:
            curr = node(name, val=None, op=op)
            cache[name] = curr

        if left in cache:
            curr.left = cache[left]
        else:
            curr.left = node(left)
            cache[left] = curr.left

        if right in cache:
            curr.right = cache[right]
        else:
            curr.right = node(right)
            cache[right] = curr.right

print(cache)

#%%
print(cache["root"].print_tree())

# %%
def calc(el):
    print(el.name)
    if el.op is None:
        return el.val
    if el.left:
        left = calc(el.left)
    if el.right:
        right = calc(el.right)

    print(el.name, left, type(left), right, type(right))
    match el.op:
        case "+":
            return left + right
        case "-":
            return left - right
        case "*":
            return left * right
        case "/":
            return left / right


calc(cache["root"])


# %%
