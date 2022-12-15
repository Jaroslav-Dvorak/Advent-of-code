in_file = __file__.split(".")[0].split("/")[-1]+".txt"
with open(in_file, "r") as f:
    raw = f.read()

slicesize = 4
i = 0
scan = raw[i:i+slicesize]
while len(set(scan)) != slicesize:
    scan = raw[i:i+slicesize]
    i += 1

print("T1:", i+slicesize-1)

##########################################################

slicesize = 14
i = 0
scan = raw[i:i+slicesize]
while len(set(scan)) != slicesize:
    scan = raw[i:i+slicesize]
    i += 1

print("T2:", i+slicesize-1)
