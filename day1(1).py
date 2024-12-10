contents = []
with open("input.txt") as file:
    for line in file.readlines():
        contents.append(line.replace('\n', '').split('   '))

list1 = [int(x[0]) for x in contents]
list2 = [int(x[1]) for x in contents]
list1.sort()
list2.sort()

totalDif = 0
for i in range(len(contents)):
    totalDif += abs(list1[i] - list2[i])
print(totalDif)