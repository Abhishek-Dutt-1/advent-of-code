#%%
f = open("input.txt", "r")
lines = f.readlines()
print(lines)
f.close()


#%%
sum_pri = 0
for line in lines:
    row = line.replace("\n", "")
    # print(row, len(row))
    assert len(row) % 2 == 0
    left = row[:len(row)//2]
    right = row[len(row)//2:]
    # print(left, right, row)
    assert len(left) + len(right) == len(row)
    left = set(left) 
    right = set(right) 
    common = left.intersection(right)
    # print(common)
    for item in common:
        if ord(item) >= 65 and ord(item) <= 90:
            # Uppercase
            sum_pri += ord(item) - 65 + 27
        elif ord(item) >= 97 and ord(item) <= 122:
            # Lowercase
            sum_pri += ord(item) - 97 + 1
        else:
            adfasdf


print(sum_pri)

 

#%%
sum_pri = 0
one = None
two = None
three = None
for ind, line in enumerate(lines):
    row = line.replace("\n", "")
    print(ind+1, row)
    if not one:
        one = row
        continue
    
    if not two:
        two = row
        continue

    three = row
    if (ind+1) % 3 == 0:
        print(3)
        print(one, two, three)
        common = set(one).intersection(set(two)).intersection(set(three))
        assert len(common) == 1
        for item in common:
            if ord(item) >= 65 and ord(item) <= 90:
                # Uppercase
                sum_pri += ord(item) - 65 + 27
            elif ord(item) >= 97 and ord(item) <= 122:
                # Lowercase
                sum_pri += ord(item) - 97 + 1
            else:
                adfasdf


        one = None
        two = None
        three = None

print(sum_pri)
 

# %%
