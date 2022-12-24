#%%
f = open("input.txt", "r")
lines = f.readlines()
print(lines)
f.close()


# %%

max_cal = 0 
cur_cal = 0
all_cal = []
for line in lines:
    cal = line.replace("\n", "")
    if cal:
        cur_cal += int(cal)
    else:
        max_cal = max(max_cal, cur_cal)
        all_cal.append(cur_cal)
        cur_cal = 0

print(max_cal)
all_cal = sorted(all_cal, reverse=True)


# %%
sum(all_cal[:3])

# %%
