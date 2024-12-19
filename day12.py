array = []
with open("input.txt") as file:
    for line in file.readlines():
        array.append([x for x in line.replace('\n', '')])

