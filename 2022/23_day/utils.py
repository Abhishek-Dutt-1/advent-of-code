# coord_cache = set()


class elf:
    dirs = ["N", "S", "W", "E"]
    curr_dir = 0
    no_need_to_move = False
    proposed_coord = None
    coord = None

    def __init__(self, coord):
        self.coord = coord

    def is_move_needed(self, elf_list):
        # NW, N, NE
        y, x = self.coord
        for ny, nx in [
            (y - 1, x - 1),
            (y - 1, x),
            (y - 1, x + 1),
            (y, x + 1),
            (y + 1, x + 1),
            (y + 1, x),
            (y + 1, x - 1),
            (y, x - 1),
        ]:
            # print("Checking:", ny, nx)
            if not self._is_empty((ny, nx), elf_list):
                return True

        return False

    def _is_empty(self, ncoord, elf_list):
        for elf in elf_list:
            if ncoord == elf.coord:
                # print("Not Empty:", ncoord)
                return False
        # print("Empty:", ncoord)
        return True

    def check_dir(self, cur_dir, elf_list) -> str:

        cur_dir = cur_dir % len(self.dirs)

        dir = self.dirs[cur_dir]

        y, x = self.coord

        match dir:
            case "N":
                ncoord1 = (y - 1, x - 1)
                ncoord2 = (y - 1, x)
                ncoord3 = (y - 1, x + 1)
            case "S":
                ncoord1 = (y + 1, x - 1)
                ncoord2 = (y + 1, x)
                ncoord3 = (y + 1, x + 1)
            case "W":
                ncoord1 = (y - 1, x - 1)
                ncoord2 = (y, x - 1)
                ncoord3 = (y + 1, x - 1)
            case "E":
                ncoord1 = (y - 1, x + 1)
                ncoord2 = (y, x + 1)
                ncoord3 = (y + 1, x + 1)

        if (
            self._is_empty(ncoord1, elf_list)
            and self._is_empty(ncoord2, elf_list)
            and self._is_empty(ncoord3, elf_list)
        ):
            # print("Proposing in dir", dir)
            return dir
        else:
            # print("NOT Proposing in dir", dir)
            return False

    def propose(self, dir):
        y, x = self.coord
        match dir:
            case "N":
                ncoord = (y - 1, x)
            case "S":
                ncoord = (y + 1, x)
            case "W":
                ncoord = (y, x - 1)
            case "E":
                ncoord = (y, x + 1)

        self.proposed_coord = ncoord
        # if ncoord == (4, 35):
        #     print("PROPOSING", ncoord)
        # print("Proposing:", ncoord)
        return ncoord

    def update_curr_dir(self):
        self.curr_dir = (self.curr_dir + 1) % len(self.dirs)

    def move(self, coord):
        # print(f"Moving from {self.coord} to {coord}")
        self.coord = coord
        self.proposed_coord = None


def get_elf_list_from_input(inp):

    elf_list = []

    for i, line in enumerate(inp):
        row = line.replace("\n", "")
        # print(row)
        for j, char in enumerate(row):
            if char == "#":
                elf_list.append(elf((i, j)))

    return elf_list


PROPOSAL_CACHE = {}


def add_to_cache(coord):
    # print("Adding", coord)
    if coord not in PROPOSAL_CACHE:
        PROPOSAL_CACHE[coord] = 1
    else:
        PROPOSAL_CACHE[coord] += 1


def check_cache(coord):
    # print(coord)
    return PROPOSAL_CACHE[coord]


def clear_cache():
    global PROPOSAL_CACHE
    PROPOSAL_CACHE = {}
    # print(len(PROPOSAL_CACHE))


def get_top_most_elf(elf_list):
    top = None
    for elf in elf_list:
        if top is None:
            top = elf.coord
        top = min(top, elf.coord, key=lambda x: x[0])

    return top


def get_left_most_elf(elf_list):
    left = None
    for elf in elf_list:
        if left is None:
            left = elf.coord
        left = min(left, elf.coord, key=lambda x: x[1])

    return left


def get_right_most_elf(elf_list):
    right = None
    for elf in elf_list:
        if right is None:
            right = elf.coord
        right = max(right, elf.coord, key=lambda x: x[1])

    return right


def get_bot_most_elf(elf_list):
    bot = None
    for elf in elf_list:
        if bot is None:
            bot = elf.coord
        bot = max(bot, elf.coord, key=lambda x: x[0])

    return bot


def get_elfs_in_rect(top_left, bot_right, elf_list):
    count = 0
    for elf in elf_list:
        if (
            top_left[0] <= elf.coord[0] <= bot_right[0]
            and top_left[1] <= elf.coord[1] <= bot_right[1]
        ):
            count += 1
    return count
