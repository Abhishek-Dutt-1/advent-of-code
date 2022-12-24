#%%
from pprint import pprint
import copy

# f = open("input_2.txt", "r")
f = open("input.txt", "r")
lines = f.readlines()
print(lines)
f.close()


#%%
for line in lines:
    row = line.replace("\n", "")
    print(row)


#%%
class game:
    def read_input(self, filename):
        f = open(filename, "r")
        lines = f.readlines()
        f.close()

        row = ""
        for line in lines:
            row = line.replace("\n", "")
        return row

    dash = [["#", "#", "#", "#"]]
    plus = [
        [".", "#", "."],
        ["#", "#", "#"],
        [".", "#", "."],
    ]
    L = [
        [".", ".", "#"],
        [".", ".", "#"],
        ["#", "#", "#"]
    ]
    I = [
        ["#"],
        ["#"],
        ["#"],
        ["#"],
    ]

    box = [
        ["#", "#"],
        ["#", "#"],
    ]

    rocks = [("dash", dash), ("plus", plus), ("L", L), ("I", I), ("box", box)]
    rocks_generator = None
    rocks_count = 0
    curr_rock = None
    curr_rock_name = None
    curr_rock_pos = None

    board = [
        ["|", ".", ".", ".", ".", ".", ".", ".", "|"],  # <-- Top Left (0, 0)
        ["|", ".", ".", ".", ".", ".", ".", ".", "|"],
        ["|", ".", ".", ".", ".", ".", ".", ".", "|"],
        ["+", "-", "-", "-", "-", "-", "-", "-", "+"],  # <-- last_row = 0
    ]

    last_row = 0
    actual_last_row = 0

    jet_pattern = None
    jet_generator = None

    def __init__(self, filename):
        self.jet_pattern = self.read_input(filename)

    def begin_next_rock(self):
        if not self.rocks_generator:
            self.rocks_generator = self._get_next_rock()
        next_rock = next(self.rocks_generator)

        self.curr_rock_name = next_rock[0]
        # if next_rock[0] == "plus":
        #     print("Starting PLUS")
        next_rock = next_rock[1]

        new_empty_rows_needed = 3 - (len(self.board) - (self.last_row + 1))
        new_empty_rows_needed += len(next_rock)

        if new_empty_rows_needed < 0:
            new_empty_rows_needed = 0
        for _ in range(new_empty_rows_needed):
            self.board = [
                ["|", ".", ".", ".", ".", ".", ".", ".", "|"]
            ] + self.board

        new_y = len(self.board) - self.last_row - 1 - 3 - len(next_rock)
        self.curr_rock = next_rock
        self.curr_rock_pos = (new_y, 3)
        self.rocks_count += 1
        self.capture_frame()

    def jet_push(self):
        if not self.jet_generator:
            self.jet_generator = self._get_next_jet()
        next_jet = next(self.jet_generator)
        next_pos = self.curr_rock_pos
        if next_jet == ">":
            # print(">")
            next_pos = next_pos[0], next_pos[1] + 1
        elif next_jet == "<":
            # print("<")
            next_pos = next_pos[0], next_pos[1] - 1
        else:
            assert False, "Unknown jet pattern"

        board_patch = self._get_board_patch(
            next_pos, (len(self.curr_rock), len(self.curr_rock[0]))
        )

        if not self._intersection(self.curr_rock, board_patch):
            # Rock can move to next position
            self.curr_rock_pos = next_pos
        else:
            # Rock cant move to next pos
            # Dont do anything
            pass

        self.capture_frame()

    def check_can_go_down(self):
        next_pos = self.curr_rock_pos
        next_pos = next_pos[0] + 1, next_pos[1]
        board_patch = self._get_board_patch(
            next_pos, (len(self.curr_rock), len(self.curr_rock[0]))
        )

        return not self._intersection(self.curr_rock, board_patch)

    def move_down(self):
        next_pos = self.curr_rock_pos
        next_pos = next_pos[0] + 1, next_pos[1]
        self.curr_rock_pos = next_pos
        self.capture_frame()

    def freeze_rocks(self):
        # Rock cant move to next pos
        self._add_rock_to_board(self.curr_rock, self.curr_rock_pos)
        new_last_row = len(self.board) - self.curr_rock_pos[0] - 1
        self.last_row = max(new_last_row, self.last_row)


    def _add_rock_to_board(self, next_rock, pos):
        for i, row in enumerate(next_rock):
            for j, col in enumerate(row):
                if col == "#":
                    self.board[pos[0] + i][pos[1] + j] = col

    def _delete_rock_from_boad(self, next_rock, pos):
        for i, row in enumerate(next_rock):
            for j, col in enumerate(row):
                if col == "#":
                    self.board[pos[0] + i][pos[1] + j] = "."


    def _get_next_rock(self):
        i = 0
        while True:
            yield self.rocks[i]
            i += 1
            i = i % len(self.rocks)

    def _get_next_jet(self):
        i = 0
        while True:
            yield self.jet_pattern[i]
            i += 1
            i = i % len(self.jet_pattern)

    def _get_board_patch(self, topleft, botright):
        # print(f"{len(self.board)}, {topleft}, {botright}")
        board_patch = []
        for i in range(topleft[0], topleft[0] + botright[0]):
            board_patch.append(
                self.board[i][topleft[1] : topleft[1] + botright[1]]
            )
        return board_patch

    def _intersection(self, patch1, patch2):
        assert len(patch1) == len(patch2)
        assert len(patch1[0]) == len(patch2[0])

        for i in range(len(patch1)):
            for j in range(len(patch1[0])):
                if patch1[i][j] != "#":
                    continue
                if patch2[i][j] != ".":
                    return True
        return False  # <-- All good, no intersection

    # def _clear_board(self, topleft, botright):
    #     for i in range(topleft[0], topleft[0] + botright[0]):
    #         for j in range(topleft[1], topleft[1] + botright[1]):
    #             self.board[i][j] = "."

    def print_board(self, patch=None):
        if not patch:
            patch = self.board
        for row in patch:
            print("".join(row))

    movie = []
    def capture_frame(self):
        return
        self._add_rock_to_board(self.curr_rock, self.curr_rock_pos)
        if self.curr_rock_name == "plus":
            # self.print_board()
            # print()
            frame = copy.deepcopy(self.board)
            frame2 = []
            str2int = {"|":1, "+": 1, "-": 1, ".": 100, "#": 23}
            f_h = min(len(frame), 20)
            for i in range(f_h):
                frame2.append([])
                for j in range(len(frame[0])):
                    frame2[i].append(str2int[frame[i][j]])
            self.movie.append(frame2)
        self._delete_rock_from_boad(self.curr_rock, self.curr_rock_pos)
        # self._clear_board(
        #     self.curr_rock_pos, (len(self.curr_rock), len(self.curr_rock[0]))
        # )




#%%
# g = game("input.txt")
g = game("input_2.txt")


# %%
from time import time

# t1 = time()
# while g.rocks_count != 2022:
while g.rocks_count != 1000000000000:
    if g.rocks_count % 100000 == 0:
        print(time() - t1, "sec")
        t1 = time()
    if g.last_row >= 200:
        # g.print_board()
        g.board = g.board[:len(g.board) - 100]
        g.last_row = g.last_row - 100
        g.actual_last_row += 100
    g.begin_next_rock()
    hit_bottom = False
    while not hit_bottom:
        g.jet_push()
        if g.check_can_go_down():
            g.move_down()
        else:
            g.freeze_rocks()
            hit_bottom = True
            # print(g.rocks_count)
            # print(g.last_row)
            # g.print_board()

# %%
g.print_board()

#%%
print(g.actual_last_row, g.last_row, g.actual_last_row + g.last_row)

# 3195 <-- too low
# 3196 <-- too low
# 3197 <-- Right

10000000,00,000

# %%
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

arr=[]
for i in range(100):
    c=np.random.rand(10,10)        
    arr.append(c)

arr = g.movie
fig = plt.figure()
i=0
im = plt.imshow(arr[0], animated=True)
def updatefig(*args):
    global i
    i += 1
    # if (i<99):
    #     i += 1
    # else:
    #     i=0
    im.set_array(arr[i])
    return im,
ani = animation.FuncAnimation(fig, updatefig,  blit=True, interval=50)
plt.show()
# %%
