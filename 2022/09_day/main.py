#%%
f = open("input.txt", "r")
lines = f.readlines()
print(lines)
f.close()


#%%
for line in lines:
    row = line.replace("\n", "")
    print(row)


#%%
def touching(hx, hy, tx, ty):
    return abs(hx - tx) <= 1 and abs(hy - ty) <= 1


def check_if_cross(hx, hy, tx, ty):
    if hx == tx:
        assert abs(hy - ty) == 2
        if hy > ty:
            return 1, "ty"
        else:
            return -1, "ty"

    if hy == ty:
        assert abs(hx - tx) == 2
        if hx > tx:
            return 1, "tx"
        else:
            return -1, "tx"

    return 0, None


def check_if_diag(hx, hy, tx, ty):
    x, y = hx - tx, hy - ty
    assert x != 0 and y != 0
    if x > 0 and y > 0:
        return True, 1, 1
    if x < 0 and y > 0:
        return True, -1, 1
    if x < 0 and y < 0:
        return True, -1, -1
    if x > 0 and y < 0:
        return True, 1, -1
    return False, 0, 0


def move_tail(hx, hy, tx, ty):
    if touching(hx, hy, tx, ty):
        return tx, ty
    unit, dir = check_if_cross(hx, hy, tx, ty)
    if unit:
        if dir == "ty":
            return tx, ty + unit
        if dir == "tx":
            return tx + unit, ty

    check, deltax, deltay = check_if_diag(hx, hy, tx, ty)
    if check:
        return tx + deltax, ty + deltay


hx = 0
hy = 0
tx = 0
ty = 0
cache = set()
for line in lines:
    row = line.replace("\n", "")
    print(row)
    match row.split(" "):
        case ["R", count]:
            for step in range(int(count)):
                hx += 1
                tx, ty = move_tail(hx, hy, tx, ty)
                print(hx, hy, tx, ty)
                cache.add((tx, ty))
            continue
        case ["L", count]:
            for step in range(int(count)):
                hx -= 1
                tx, ty = move_tail(hx, hy, tx, ty)
                print(hx, hy, tx, ty)
                cache.add((tx, ty))
            continue
        case ["U", count]:
            for step in range(int(count)):
                hy += 1
                tx, ty = move_tail(hx, hy, tx, ty)
                print(hx, hy, tx, ty)
                cache.add((tx, ty))
            continue
        case ["D", count]:
            for step in range(int(count)):
                hy -= 1
                tx, ty = move_tail(hx, hy, tx, ty)
                print(hx, hy, tx, ty)
                cache.add((tx, ty))
            continue
        case _:
            raise ValueError("Unknown movemebt")




print(len(cache))

# %%
x = []
y = []
for coord in cache:
    x.append(coord[0])
    y.append(coord[1])

max(x), min(x), max(y), min(y)

# %%
