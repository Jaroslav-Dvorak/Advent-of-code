in_file = __file__.split(".")[0].split("/")[-1]+".txt"
with open(in_file, "r") as f:
    raw = f.read()

alphanum = "abcdefghijklmnopqrstuvwxyz"
alphanum += alphanum.upper()
priorities = {letter: priority for priority, letter in enumerate(alphanum, 1)}

sum_of_priorities = 0
rucksacks = raw.splitlines()
for rucksack in rucksacks:
    items_in_compart = len(rucksack)//2
    first_compart = set(rucksack[0:items_in_compart])
    second_compart = set(rucksack[items_in_compart:])
    common_item = tuple(first_compart & second_compart)[0]
    sum_of_priorities += priorities[common_item]

print("T1:", sum_of_priorities)

#####################################################################################

sum_of_priorities = 0
rucksacks = raw.splitlines()
batches = []
while rucksacks:
    found = False
    rucksack_1 = rucksacks[0]
    rucksack_1_set = set(rucksack_1)
    for rucksack_2 in rucksacks:
        if rucksack_1 is rucksack_2:
            continue
        rucksack_2_set = set(rucksack_2)
        for rucksack_3 in rucksacks:
            if (rucksack_3 is rucksack_1) or (rucksack_3 is rucksack_2):
                continue
            rucksack_3_set = set(rucksack_3)
            batch = rucksack_1_set & rucksack_2_set & rucksack_3_set
            if len(batch) == 1:
                batch = tuple(batch)[0]
                sum_of_priorities += priorities[batch]
                rucksacks.remove(rucksack_1)
                rucksacks.remove(rucksack_2)
                rucksacks.remove(rucksack_3)
                found = True
                break
        if found:
            break

print("T2:", sum_of_priorities)
