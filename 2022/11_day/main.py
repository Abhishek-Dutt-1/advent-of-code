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
class monkey:
    def __init__(self, name, items, ops, test_func):
        self.name = name
        self.items = items
        self.ops = ops
        self.test_func = test_func
        self.insp_count = 0

    def get_item(self):
        if self.items:
            self.insp_count += 1
            item = self.items[0]
            self.items = self.items[1:]
            # print(item, self.items)
            return item
        return False


#%%
m0 = monkey(
    0, 
    [83, 62, 93], 
    lambda old: old * 17, 
    lambda worry: 1 if worry % 2 == 0 else 6
)

m1 = monkey(
    1, 
    [90, 55], 
    lambda old: old + 1, 
    lambda worry: 6 if worry % 17 == 0 else 3
)


m2 = monkey(
    2, 
    [91, 78, 80, 97, 79, 88], 
    lambda old: old + 3, 
    lambda worry: 7 if worry % 19 == 0 else 5
)


m3 = monkey(
    3, 
    [64, 80, 83, 89, 59], 
    lambda old: old + 5, 
    lambda worry: 7 if worry % 3 == 0 else 2
)

m4 = monkey(
    4, 
    [98, 92, 99, 51], 
    lambda old: old * old, 
    lambda worry: 0 if worry % 5 == 0 else 1
)

m5 = monkey(
    5, 
    [68, 57, 95, 85, 98, 75, 98, 75], 
    lambda old: old + 2,
    lambda worry: 4 if worry % 13 == 0 else 0
)

m6 = monkey(
    6, 
    [74],
    lambda old: old + 4,
    lambda worry: 3 if worry % 7 == 0 else 2
)

m7 = monkey(
    7, 
    [68, 64, 60, 68, 87, 80, 82],
    lambda old: old * 19,
    lambda worry: 4 if worry % 11 == 0 else 5
)


# %%
M = [m0, m1,m2,m3,m4,m5,m6,m7]
for cc in range(10000):
    print(cc)
    for m in M:
        # print("New moneky", m)
        cnt = 0
        # while cnt < 100:
        while True:
            cnt += 1
            item = m.get_item()
            if not isinstance(item, bool):
                # print(item, " ",end="")
                worry = m.ops(item)
                # worry = worry // 3
                worry = worry % (2*17*19*3*5*13*7*11)
                other_monkey = m.test_func(worry)
                M[other_monkey].items.append(worry)
                # print(m.name, "-- throwing ", worry, "to ", other_monkey, M[other_monkey].items)
            else:
                # print("breaking")
                break


# %%
store = []
for m in M:
    print(m.insp_count)
    store.append(m.insp_count)

store = sorted(store)
print(store)
print(store[-1]*store[-2])


# %%
327*345

2*17*19*3*5*13*7*11
# %%
