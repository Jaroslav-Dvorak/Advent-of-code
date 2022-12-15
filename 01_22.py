
in_file = __file__.split(".")[0].split("/")[-1]+".txt"
with open(in_file, "r") as f:
    raw = f.read()

elfs = raw.split("\n\n")
elfs = [elf.split("\n") for elf in elfs]
sums_of_cals = []
for elf in elfs:
    cals_per_elf = []
    for cal in elf:
        try:
            cal_int = int(cal)
        except ValueError:
            continue
        else:
            cals_per_elf.append(cal_int)

    sums_of_cals.append(sum(cals_per_elf))

res = max(sums_of_cals)

print("T1:", res)

#############################################

sorted_sums_of_cals = sorted(sums_of_cals)
sum_of_max_3 = sum(sorted_sums_of_cals[-3:])
print("T2:", sum_of_max_3)
