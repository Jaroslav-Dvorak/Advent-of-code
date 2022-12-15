from copy import deepcopy
file = __file__.split(".")[0].split("/")[-1] + ".txt"

with open(file, "r") as f:
    raw = f.read()

# [Q] [J]                         [H]
# [G] [S] [Q]     [Z]             [P]
# [P] [F] [M]     [F]     [F]     [S]
# [R] [R] [P] [F] [V]     [D]     [L]
# [L] [W] [W] [D] [W] [S] [V]     [G]
# [C] [H] [H] [T] [D] [L] [M] [B] [B]
# [T] [Q] [B] [S] [L] [C] [B] [J] [N]
# [F] [N] [F] [V] [Q] [Z] [Z] [T] [Q]
#  1   2   3   4   5   6   7   8   9

lines = raw.splitlines()
cargo = lines[:8]
crates = [[] for _ in range(9)]
for row in cargo:
    f_row = ""
    for r in range(1, len(row), 4):
        f_row += row[r]
    for index, crate in enumerate(f_row):
        if crate != " ":
            crates[index].append(crate)

crates = [crate[::-1] for crate in crates]
crates.insert(0, None)
crates_t2 = deepcopy(crates)

instructions = lines[10:]
f_instructs = {"move": [], "from": [], "to": []}
for instr in instructions:
    instr = instr.split()
    f_instructs[instr[0]].append(int(instr[1]))
    f_instructs[instr[2]].append(int(instr[3]))
    f_instructs[instr[4]].append(int(instr[5]))

for amount, get, put in zip(f_instructs["move"], f_instructs["from"], f_instructs["to"]):
    for _ in range(amount):
        on_crain = crates[get].pop(-1)
        crates[put].append(on_crain)

ans = ""
for crate in crates:
    if crate is not None:
        ans += crate[-1]

print("T1:", ans)

##########################################################################################

crates = crates_t2

for amount, get, put in zip(f_instructs["move"], f_instructs["from"], f_instructs["to"]):
    on_crain = crates[get][-amount:]
    crates[get] = crates[get][:-amount]
    crates[put].extend(on_crain)

ans = ""
for crate in crates:
    if crate is not None:
        ans += crate[-1]

print("T2:", ans)
