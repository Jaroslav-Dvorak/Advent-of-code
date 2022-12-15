in_file = __file__.split(".")[0].split("/")[-1]+".txt"
with open(in_file, "r") as f:
    raw = f.read()

legend = {"A": "R", "B": "P", "C": "S", "X": "R", "Y": "P", "Z": "S"}
for orig, repl in legend.items():
    repl_raw = raw.replace(orig, repl)

lines = repl_raw.splitlines()
rounds = [line.split() for line in lines]
score = 0

for r in rounds:
    oponent = r[0]
    me = r[1]
    if oponent == me:
        score += 3
    if me == "R":
        score += 1
        if oponent == "S":
            score += 6
    if me == "P":
        score += 2
        if oponent == "R":
            score += 6
    if me == "S":
        score += 3
        if oponent == "P":
            score += 6

print("T1:", score)

########################################################################

with open("02_22.txt", "r") as f:
    raw = f.read()

legend = {"A": "R", "B": "P", "C": "S"}
# {"X": "R", "Y": "P", "Z": "S"}
for orig, repl in legend.items():
    repl_raw = raw.replace(orig, repl)

lines = repl_raw.splitlines()
rounds = [line.split() for line in lines]
score = 0

for r in rounds:
    oponent = r[0]
    me = r[1]
    if me == "X":
        if oponent == "R": me = "S"
        elif oponent == "P": me = "R"
        elif oponent == "S": me = "P"
    elif me == "Y":
        me = oponent
    elif me == "Z":
        if oponent == "R": me = "P"
        elif oponent == "P": me = "S"
        elif oponent == "S": me = "R"

    if oponent == me:
        score += 3
    if me == "R":
        score += 1
        if oponent == "S":
            score += 6
    if me == "P":
        score += 2
        if oponent == "R":
            score += 6
    if me == "S":
        score += 3
        if oponent == "P":
            score += 6

print("T2:", score)
