#%%
from pprint import pprint
import utils

f = open("input.txt", "r")
# f = open("input_2.txt", "r")
# f = open("input_3.txt", "r")
lines = f.readlines()
print(lines)
f.close()


#%%
for line in lines:
    row = line.replace("\n", "")
    print(row)


# %%
total_elfs = 0
proposed_move_coords = {}

elf_list = utils.get_elf_list_from_input(lines)
total_elfs = len(elf_list)

no_need_to_move = 0
moves_count = 0
while no_need_to_move != total_elfs:
    # if moves_count == 10:
    #     break
    cant_move_surrounded = 0
    cant_move_tie = 0
    no_need_to_move = 0
    elfs_moved = 0

    print("=" * 20)
    print("Starting Proposal Phase", moves_count+1)
    utils.clear_cache()
    # print("CACHE:", utils.PROPOSAL_CACHE)
    for elf in elf_list:
        # print("-" * 20)
        # print("- Starting New Elf -", elf.coord)
        if elf.is_move_needed(elf_list):
            elf.no_need_to_move = False
            cur_dir = elf.curr_dir
            # print(cur_dir)
            if dir := elf.check_dir(cur_dir, elf_list):
                coord = elf.propose(dir)
                utils.add_to_cache(coord)
            elif dir := elf.check_dir(cur_dir + 1, elf_list):
                coord = elf.propose(dir)
                utils.add_to_cache(coord)
            elif dir := elf.check_dir(cur_dir + 2, elf_list):
                coord = elf.propose(dir)
                utils.add_to_cache(coord)
            elif dir := elf.check_dir(cur_dir + 3, elf_list):
                coord = elf.propose(dir)
                utils.add_to_cache(coord)
            else:
                elf.cant_move_surrounded = True
                # print("CANT MOVE MAN")
                cant_move_surrounded += 1
            # elf.update_curr_dir()   # <-- maybe this needs to be in else part too
        else:
            # print(elf.coord, "No NEED to MOVE")
            elf.no_need_to_move = True
            no_need_to_move += 1

        elf.update_curr_dir()  # <-- maybe this needs to be in else part too

    # print("=" * 20)
    # print("Starting MOVE Phase")
    # print("CACHE:", utils.PROPOSAL_CACHE)
    for elf in elf_list:
        if not elf.no_need_to_move:
            if (
                elf.proposed_coord is not None
                and utils.check_cache(elf.proposed_coord) == 1
            ):
                elf.move(elf.proposed_coord)
                elfs_moved += 1
            else:
                elf.proposed_coord = None
                cant_move_tie += 1
        else:
            elf.proposed_coord = None

    moves_count += 1

print(f"Made {moves_count} moves!")

top = utils.get_top_most_elf(elf_list)
left = utils.get_left_most_elf(elf_list)
right = utils.get_right_most_elf(elf_list)
bot = utils.get_bot_most_elf(elf_list)
print(top, left, right, bot)

top_left = top[0], left[1]
bot_right = bot[0], right[1]

print(top_left, bot_right)

elf_count = utils.get_elfs_in_rect(top_left, bot_right, elf_list)
print("elf_count: ", elf_count)

rows, cols = bot_right[0] - top_left[0] + 1, bot_right[1] - top_left[1] + 1
print(f"rows={rows}, cols={cols}")
total_places = rows * cols

print("total_palces: ", total_places)
empty_spaces = total_places - elf_count
print(empty_spaces)

grid = [["."] * cols for _ in range(rows)]


#%%

for elf in elf_list:
    grid[elf.coord[0] - top_left[0]][elf.coord[1] - top_left[1]] = "#"

pprint(grid)

# %%
import pandas as pd

df = pd.DataFrame(grid)
