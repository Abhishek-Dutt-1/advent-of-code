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
check = [20, 60, 100, 140, 180, 220]
signal_str = 0
X = 1
clock = 0
for line in lines:
    row = line.replace("\n", "")
    print(row)
    match row.split():
        case ["noop"]:
            clock += 1
            continue
        case ["addx", num]:
            clock += 1
            if clock in check:
                signal_str += clock * X
            clock += 1
            if clock in check:
                signal_str += clock * X
            X += int(num)


print(signal_str, X, clock)

# %%
len(lines)

# %%
crt = ["  "] * 240
char = "||"
X = 1
clock = 1
line_num = 0
for line in lines:
    row = line.replace("\n", "")
    print(clock, X, X <= clock and clock <= X + 2)
    if clock > 40:
        clock = clock % 40
        line_num += 1
    match row.split():
        case ["noop"]:
            if X <= clock and clock <= X + 2:
                crt[(line_num * 40) + clock - 1] = char
            clock += 1
            continue
        case ["addx", num]:
            if X <= clock and clock <= X + 2:
                crt[(line_num * 40) + clock - 1] = char
            clock += 1
            if X <= clock and clock <= X + 2:
                crt[(line_num * 40) + clock - 1] = char
            clock += 1
            X += int(num)


print(X, clock)

# %%
print("".join(crt[0:40]))
print("".join(crt[40:80]))
print("".join(crt[80:120]))
print("".join(crt[120:160]))
print("".join(crt[160:200]))
print("".join(crt[200:240]))

# %%
