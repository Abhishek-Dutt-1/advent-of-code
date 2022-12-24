#%%
f = open("input.txt", "r")
lines = f.readlines()
print(lines)
f.close()


#%%
def check_overlap(l_s, l_e, r_s, r_e):
    # check if l overlaps r
    if l_s <= r_s and l_e >= r_e:
        return True
    if r_s <= l_s and r_e >= l_e:
        return True
    return False

overlap_count = 0
for line in lines:
    row = line.replace("\n", "")
    left, right = row.split(",")
    left_s, left_e = left.split("-")
    right_s, right_e = right.split("-")
    left_s = int(left_s)
    left_e = int(left_e)
    right_s = int(right_s)
    right_e = int(right_e)
    if check_overlap(left_s, left_e, right_s, right_e):
        overlap_count += 1

    print(left, type(left_s), left_e, right, row)

print(overlap_count)

 
#%%
def check_any_overlap(l_s, l_e, r_s, r_e):
    if l_s <= r_s and l_e >= r_s:
        return True
    if l_s <= r_e and l_e >= r_e:
        return True
    if r_s <= l_s and r_e >= l_s:
        print(l_s, l_e, r_s, r_e)
        return True
    # if r_s <= l_e and r_e >= l_e:
    #     return True
    return False

overlap_count = 0
for line in lines:
    row = line.replace("\n", "")
    left, right = row.split(",")
    left_s, left_e = left.split("-")
    right_s, right_e = right.split("-")
    left_s = int(left_s)
    left_e = int(left_e)
    right_s = int(right_s)
    right_e = int(right_e)
    if check_any_overlap(left_s, left_e, right_s, right_e):
        overlap_count += 1

    print(left, type(left_s), left_e, right, row)

print(overlap_count)
 
# %%
