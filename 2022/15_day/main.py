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
#%%
sensors = []
beacons = []
for line in lines:
    row = line.replace("\n", "")
    print(row)
    row = row.split()
    s = int(row[2].split("=")[1][:-1]), int(row[3].split("=")[1][:-1])
    b = int(row[8].split("=")[1][:-1]), int(row[9].split("=")[1])
    sensors.append(s)
    beacons.append(b)


# %%
# print(sensors)
# print(beacons)
xy = sensors + beacons
# print(xy)
max_xy = (
    max(xy, key=lambda item: item[0])[0],
    max(xy, key=lambda item: item[1])[1],
)
print(max_xy)

min_xy = (
    min(xy, key=lambda item: item[0])[0],
    min(xy, key=lambda item: item[1])[1],
)
print(min_xy)


# %%
for x, y in sensors:
    print(" ", x, y, end="")

print("=")
for x, y in beacons:
    print(" ", x, y, end="")


# %%
y = 2000000
y_ranges = []
for s, b in zip(sensors, beacons):
    # dist b/w s and b
    sb = abs(s[0] - b[0]) + abs(s[1] - b[1])
    # vertical distance b/w y and s
    sy = abs(s[1] - y)
    if sy <= sb:
        # print(sb, sy)
        lx = s[0] - (sb - sy)
        rx = s[0] + (sb - sy)
        # print(lx, rx)
        y_ranges.append((lx, rx))

y_ranges = sorted(y_ranges, key=lambda item: item[0])
pprint(y_ranges)

# %%

fil = []

tmp = y_ranges[:]
for ind in range(len(tmp) - 1):
    f = tmp[ind]
    s = tmp[ind + 1]
    new = ()
    if s[1] <= f[1]:
        # second is completely inside first, take first, drop second
        new = [f]
        tmp.pop(ind+1)
    elif s[0] <= f[1] and s[1] >= f[1]:
        # Second is out of first partially, merge
        new = [(f[0], s[1])]
        tmp.pop(ind)
        tmp.pop(ind)
    elif s[0] > f[1] and s[1] > f[1]:
        # No overlap b/w first and second, keep both
        new = [f, s]
    else:
        assert False, "This should not happen"
    
    fil += new


#%%

fil = []
f = y_ranges[0]
ctr = 1
Flag = True         #<---- Flag is not needed, tbd
while True and Flag:
    s = y_ranges[ctr]
    print(ctr, f, s)
    new = None
    if s[1] <= f[1]:
        # second is completely inside first, take first, drop second
        print("Completely overlap")
        ctr += 1
        continue
    elif s[0] <= f[1] and s[1] >= f[1]:
        # Second is out of first partially, merge
        print("Partial overlap, merge")
        f = (f[0], s[1])
        ctr += 1
        continue
    elif s[0] > f[1] and s[1] > f[1]:
        # No overlap b/w first and second, keep both
        print("No overlap")
        fil.append(f)
        f = s
        ctr += 1
        continue
    else:
        assert False, "This should not happen"
    

print(fil)

#%%

final = (-10379, 4908902)
# final = (-1, 2)
print(final[1] - final[0] + 1)
# 4919282 <-- TOO HIGH

# FORGOT TO SUBTRACT 4 BEACONS ON y=2000000
pprint(sorted(beacons, key=lambda item: item[1]))
print(final[1] - final[0] + 1 - 4)
# 4919278 <-- too low
print(final[1] - final[0] + 1 - 3)

4919278
4919279
4919280
4919281 <-- Right

#%%
################ PART 2 ##################################
from pprint import pprint
f = open("input_2.txt", "r")
# f = open("input.txt", "r")
lines = f.readlines()
print(lines)
f.close()


#%%
for line in lines:
    row = line.replace("\n", "")
    print(row)

