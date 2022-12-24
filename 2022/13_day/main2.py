#%%
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
class node:
    def __init__(self, type, val):
        self.type = type
        self.val = val
        self.children = []

    def __str__(self, level=0):
        s = "\t" * level + f"{self.type}-{self.val}\n"
        for child in self.children:
            s += child.__str__(level + 1)
        return s


one = "[[[[2]],[2,[3],[9,3],10],8],[[9,[5,7,5,5],6,8],[[],7,7,2]],[[]]]"
two = "[[[0,[5,6,5],[0,4,1]],[],[3],[]],[5,0,1],[1,3,6,[1,[7,4]],10],[]]"
one = "[[[3]], [1]]"
two = "[3, 1]"
one = "[1,1,3,1,1]"
two = "[1,1,5,1,1]"

one = "[[1],[2,3,4]]"
two = "[[1],4]"

one = "[9]"
two = "[[8,7,6]]"

one = "[[4,4],4,4]"
two = "[[4,4],4,4,4]"

one = "[7,7,7,7]"
two = "[7,7,7]"

one = "[]"
two = "[3]"

one = "[[[]]]"
two = "[[]]"

one = "[1,[2,[3,[4,[5,6,7]]]],8,9]"
two = "[1,[2,[3,[4,[5,6,0]]]],8,9]"

one = "[[[3,8],[0,8,[],6]]]"
two = "[[],[[6],6,[5]]]"

# one = "[[[3,8],[]]]"
# two = "[[],[[]]]"

one = eval(one)
two = eval(two)

def tree(parent, el):
    for e in el:
        if type(e) is int:
            parent.children.append(node("int", int(e)))
        if type(e) is list:
            parent.children.append(node("list", "."))
            child = parent.children[-1]
            tree(child, e)


root1 = node("list", "ROOT")
tree(root1, one)
root2 = node("list", "ROOT")
tree(root2, two)

print(root1)
print(root2)

def compare(r1, r2):
    b = True
    if r1.type == "int" and r2.type == "int":
        return r1.val <= r2.val
        # b = b and r1.val <= r2.val

    if r1.type == "list" and r2.type == "list":
        # print(r1.val, r2.val)
        while r1.children or r2.children:
            if not r1.children and not r2.children:
                b = b and True

            if r1.children:
                r1_child = r1.children.pop(0)
            else:
                # print("1")
                return True

            if r2.children:
                r2_child = r2.children.pop(0)
            else:
                # print("2")
                return False

            tmp = compare(r1_child, r2_child)
            if not tmp:
                return False
            b = b and tmp

    if r1.type == "int" and r2.type == "list":
        if not r2.children:
            return False
        b = b and compare(r1, r2.children.pop(0))

    if r1.type == "list" and r2.type == "int":
        if not r1.children:
            return True
        b = b and compare(r1.children.pop(0), r2)

    return b

print(compare(root1, root2))


# %%
# f = open("input.txt", "r")
f = open("input_2.txt", "r")
# f = open("input_3.txt", "r")
lines = f.readlines()
# print(lines)
f.close()

total_rows = len(lines)
idx = 0
ctr = 0
sum = 0
while ctr < total_rows:
    print("-"*10)
    idx += 1
    one = lines[ctr].replace("\n", "")
    two = lines[ctr+1].replace("\n", "")
    print(one, two)

    one = eval(one)
    two = eval(two)

    root1 = node("list", "ROOT")
    tree(root1, one)
    root2 = node("list", "ROOT")
    tree(root2, two)

    tmp =  compare(root1, root2)
    print(tmp)
    if tmp:
        # print(one, two)
        print(ctr+1, ctr+2, ":", idx)
        sum += idx

    ctr += 3

print(sum)

# %%
