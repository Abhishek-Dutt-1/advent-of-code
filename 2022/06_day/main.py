#%%
f = open("input.txt", "r")
lines = f.readlines()
print(lines)
f.close()


#%%
for line in lines:
    row = line.replace("\n", "")
    print(row)


# %%
row

#%%
print(len(row))

# %%
for char in range(len(row)-3):
    print(char)

# %%

# t = "aabcde"
t = row
for ind in range(len(t)-3):
    a = t[ind]
    b = t[ind+1]
    c = t[ind+2]
    d = t[ind+3]
    print(a, b, c, d)
    s = set([a, b, c, d])
    print(s)
    if len(s) == 4:
        print(ind+1+3)
        break


# %%
1239
1238 <-- Correct

#%%
t = row
for ind in range(len(t)-3):
    tmp = []
    for i in range(14):
        tmp.append(t[ind+i])
    s = set(tmp)
    print(s)
    if len(s) == 14:
        print(ind+1+13)
        break


# %%
3037 <-- Correct
