import re

file = open("input.txt")
data = file.read()
file.close()

expression = r"mul\([0-9]+,[0-9]+\)|don't\(\)|do\(\)"
matches = re.findall(expression, data)

enabled = True
total = 0
for match in matches:
    if match == "don't()":
        enabled = False
    elif match == "do()":
        enabled = True
    elif enabled:
        match = match[4:-1].split(',')
        total += int(match[0]) * int(match[1])

print(total)