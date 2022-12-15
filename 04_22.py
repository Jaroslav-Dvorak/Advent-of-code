file = __file__.split(".")[0].split("/")[-1] + ".txt"

with open(file, "r") as f:
    raw = f.read()

lines = raw.splitlines()
areas = [area.split(",") for area in lines]
areas = [(area[0].split("-"), area[1].split("-")) for area in areas]
areas = [((int(area[0][0]), int(area[0][1])), (int(area[1][0]), int(area[1][1]))) for area in areas]

# areas = [(set(range(int(area[0][0]), int(area[0][1])+1)), (set(range(int(area[1][0]), int(area[1][1])+1)))) for area in areas]

overlaped = 0
for area in areas:
    first_start = area[0][0]
    first_end = area[0][1]
    second_start = area[1][0]
    second_end = area[1][1]

    if ((first_start <= second_start and first_end >= second_end)
        or
        (second_start <= first_start and second_end >= first_end)):
        overlaped += 1
print("T1:", overlaped)

########################################################################################################

areas = [area.split(",") for area in lines]
areas = [(area[0].split("-"), area[1].split("-")) for area in areas]
areas = [(set(range(int(area[0][0]), int(area[0][1])+1)), (set(range(int(area[1][0]), int(area[1][1])+1)))) for area in areas]

overlaped = 0
for area in areas:
    if area[0] & area[1]:
        overlaped += 1

print("T2:", overlaped)
