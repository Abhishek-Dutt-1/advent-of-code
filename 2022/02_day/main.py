#%%
f = open("input.txt", "r")
lines = f.readlines()
print(lines)
f.close()


# %%
# For ME:
# X = Rock, Y = Paper, Z = Scissors
# For OTHER:
# A = Rock, B = Paper, C = Scissors
def decide_winner(other, me):
    if other == me:
        return "DRAW"
    if me == "X" and other == "Y":
        return "OTHER"
    if me == "X" and other == "Z":
        return "ME"
    if me == "Y" and other == "Z":
        return "OTHER"
    if me == "Y" and other == "X":
        return "ME"
    if me == "Z" and other == "X":
        return "OTHER"
    if me == "Z" and other == "Y":
        return "ME"

me_2_other = {"X": "A", "Y": "B", "Z": "C"}
other_2_me = {val: key for key, val in me_2_other.items()}
shape_scores = {"X": 1, "Y": 2, "Z": 3}
total_score = 0
for line in lines:
    row = line.replace("\n", "")
    other, me = row.split(" ")
    other = other_2_me[other]
    total_score += shape_scores[me]
    winner = decide_winner(other, me)
    if winner == "ME":
        total_score += 6
    if winner == "OTHER":
        total_score += 0
    if winner == "DRAW":
        total_score += 3
   

# %%
print(total_score)


# %%
# PART 2
def get_my_hand(other, result):
    # A = Rock, B = Paper, C = Scissors
    # X = lose, Y = draw, Z = win
    if result == "Y":
        return other
    if other == "A" and result == "X":
        return "C"
    if other == "A" and result == "Z":
        return "B"
    if other == "B" and result == "X":
        return "A"
    if other == "B" and result == "Z":
        return "C"
    if other == "C" and result == "X":
        return "B"
    if other == "C" and result == "Z":
        return "A"

# A = Rock, B = Paper, C = Scissors
shape_scores = {"A": 1, "B": 2, "C": 3}
total_score = 0
for line in lines:
    row = line.replace("\n", "")
    other, result = row.split(" ")
    if result == "X":
        total_score += 0
    if result == "Y":
        total_score += 3
    if result == "Z":
        total_score += 6
    me = get_my_hand(other, result)
    total_score += shape_scores[me]

print(total_score)




# %%
