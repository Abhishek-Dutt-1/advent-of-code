#%%
# f = open("input.txt", "r")
f = open("input_2.txt", "r")
lines = f.readlines()
print(lines)
f.close()


#%%
for line in lines:
    row = line.replace("\n", "")
    print(row)



Ore => Ore robot
Ore => Clay robot
Clay => Obsidian robot
Obsidian => Geod robot