import re

file = open("input.txt")
data = file.read()
file.close()

expression = r"mul\([0-9]+,[0-9]+\)"
matches = re.findall(expression, data)
matches = [match[4:-1].split(',') for match in matches]

total = 0
for match in matches:
    total += int(match[0]) * int(match[1])
print(total)