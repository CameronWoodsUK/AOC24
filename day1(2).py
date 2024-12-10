contents = []
with open("input.txt") as file:
    for line in file.readlines():
        contents.append(line.replace('\n', '').split('   '))

list1 = [int(x[0]) for x in contents]
list2 = [int(x[1]) for x in contents]

similarityScore = 0
for item in list1:
    similarityScore += item * list2.count(item)
print(similarityScore)