#%%
# f = open("input_2.txt", "r")
f = open("input.txt", "r")
lines = f.readlines()
print(lines)
f.close()


#%%
grid = []
for line in lines:
    grid.append([])
    row = line.replace("\n", "")
    for num in row:
        grid[-1].append(int(num))

    # row = line.replace("\n", "")


#%%
# rows = 5
rows = 99
cols = rows
for i in range(rows):
    for j in range(cols):
        print(grid[i][j], end="")
    print()


#%%
class tlrb:
    def __init__(self, t, l, r, b):
        self.t = t
        self.l = l
        self.r = r
        self.b = b

    def __repr__(self):
        return f"[{self.t},{self.l},{self.r},{self.b}]"


max_heights = []
for i in range(rows):
    max_heights.append([])
    for j in range(cols):
        max_heights[-1].append(tlrb(0, 0, 0, 0))

max_heights


#%%
for i in range(rows):
    for j in range(cols):
        if i == 0:
            max_heights[i][j].t = grid[i][j]
        else:
            # TOP
            max_heights[i][j].t = max(grid[i][j], max_heights[i - 1][j].t)
        if j == 0:
            max_heights[i][j].l = grid[i][j]
        else:
            # LEFT
            max_heights[i][j].l = max(grid[i][j], max_heights[i][j - 1].l)

max_heights

#%%
for i in range(rows):
    for j in range(cols):
        i2 = rows - 1 - i
        j2 = cols - 1 - j
        if i2 == rows - 1:
            max_heights[i2][j2].b = grid[i2][j2]
        else:
            # BOTTOM
            max_heights[i2][j2].b = max(
                grid[i2][j2], max_heights[i2 + 1][j2].b
            )
        if j2 == cols - 1:
            max_heights[i2][j2].r = grid[i2][j2]
        else:
            # RIGHT
            max_heights[i2][j2].r = max(
                grid[i2][j2], max_heights[i2][j2 + 1].r
            )

max_heights


# %%
grid_2 = []
for i in range(rows):
    grid_2.append([])
    for j in range(cols):
        if i == 0 or i == rows - 1:
            grid_2[-1].append(1)
        elif j == 0 or j == cols - 1:
            grid_2[-1].append(1)
        else:
            grid_2[-1].append(0)


#%%
for i in range(rows):
    for j in range(cols):
        print(grid_2[i][j], end="")
    print()

#%%
for i in range(rows):
    for j in range(cols):
        if i == 0 or j == 0 or i == rows - 1 or j == cols - 1:
            continue
        # Top
        if grid[i][j] > max_heights[i - 1][j].t:
            grid_2[i][j] = 1

        # Left
        if grid[i][j] > max_heights[i][j - 1].l:
            grid_2[i][j] = 1

        # BOTTOM
        if grid[i][j] > max_heights[i + 1][j].b:
            grid_2[i][j] = 1

        # RIGHT
        if grid[i][j] > max_heights[i][j + 1].r:
            grid_2[i][j] = 1

# -----------------------------------------


#%%
# for i in range(rows):
#     for j in range(cols):
#         if i == 0 or j == 0 or i == rows - 1 or j == cols - 1:
#             continue
#         # Top
#         if grid_2[i - 1][j] == 1 and grid[i][j] > grid[i - 1][j]:
#             grid_2[i][j] = 1

#         # Left
#         if grid_2[i][j - 1] == 1 and grid[i][j] > grid[i][j - 1]:
#             grid_2[i][j] = 1

#         print(grid_2[i][j], end="")
#     print()


#%%
# for i in range(rows):
#     for j in range(cols):
#         i2 = rows - 1 - i
#         j2 = cols - 1 - j
#         if i2 == 0 or j2 == 0 or i2 == rows - 1 or j2 == cols - 1:
#             continue

#         # Right
#         if grid_2[i2][j2 + 1] == 1 and grid[i2][j2] > grid[i2][j2 + 1]:
#             grid_2[i2][j2] = 1

#         # Bottom
#         if grid_2[i2 + 1][j2] == 1 and grid[i2][j2] > grid[i2 + 1][j2]:
#             grid_2[i2][j2] = 1

#         # Top
#         # if grid_2[i2-1][j] == 1 and grid[i2][j2] > grid[i2-1][j2]:
#         #     grid_2[i2][j2] = 1

#         # Left
#         # if grid_2[i2][j2-1] == 1 and grid[i2][j2] > grid[i2][j2-1]:
#         #     grid_2[i2][j2] = 1

#         print(grid_2[i][j], end="")
#     print()


# %%
total = 0
for i in range(rows):
    for j in range(cols):
        total += grid_2[i][j]

print(total)


# %%
class num_tree_visible:
    def __init__(self, t, l, r, b):
        self.t = t
        self.l = l
        self.r = r
        self.b = b

    def get_score(self):
        return self.t * self.l * self.r * self.b

    def __repr__(self):
        return f"[{self.t},{self.l},{self.r},{self.b}]"


max_visible = []
for i in range(rows):
    max_visible.append([])
    for j in range(cols):
        max_visible[-1].append(num_tree_visible(0, 0, 0, 0))
max_visible


#%%
for i in range(rows):
    for j in range(cols):
        # TOP
        cnt = 1
        if i == 0:
            cnt = 0
        else:
            while i - cnt >= 0 and grid[i - cnt][j] < grid[i][j]:
                cnt += 1

        if i - cnt < 0:
            cnt -= 1

        max_visible[i][j].t = cnt

        # LEFT
        cnt = 1
        if j == 0:
            cnt = 0
        else:
            while j - cnt >= 0 and grid[i][j - cnt] < grid[i][j]:
                cnt += 1

            if j - cnt < 0:
                cnt -= 1

        max_visible[i][j].l = cnt


#%%
for i in range(rows):
    for j in range(cols):
        i2 = rows - 1 - i
        j2 = cols - 1 - j
        # RIGHT
        cnt = 1
        if j2 == cols-1:
            cnt = 0
        else:
            while j2 + cnt < cols and grid[i2][j2 + cnt] < grid[i2][j2]:
                cnt += 1

            if j2 + cnt >= cols:
                cnt -= 1

        max_visible[i2][j2].r = cnt

        # BOTTOM
        cnt = 1
        if i2 == rows - 1:
            cnt = 0
        else:
            while i2 + cnt < rows and grid[i2+cnt][j2] < grid[i2][j2]:
                cnt += 1
            if i2 + cnt >= rows:
                cnt -=1
            
        max_visible[i2][j2].b = cnt


# %%
for i in range(rows):
    for j in range(cols):
        print(max_visible[i][j].b, end="")
    print()


# %%
max_score = 0
for i in range(rows):
    for j in range(cols):
        max_score = max(max_score, max_visible[i][j].get_score())
        print(max_visible[i][j], max_visible[i][j].get_score() , "- ", end="")
    print()


# %%
max_score
# %%
