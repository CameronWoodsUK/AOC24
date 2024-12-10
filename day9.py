import re

def LastDigitIndex(lst):
    for i, c in enumerate(s[::-1]):
        if c.isdigit():
            return (len(lst)-i-1)
    return -1

diskmap = []
with open("input.txt") as file:
    for c in file.read():
        diskmap.append(int(c))

layout = []
for i, n in enumerate(diskmap):
    if i % 2 == 0:
        for x in range(n):
            layout.append(str(i//2))
    else:
        for x in range(n):
            layout.append('.')

print(layout)


while len(re.findall(r"[0-9]+[.]+", ''.join(layout))) != 1:
    layout[layout.index('.')], layout[LastDigitIndex(layout)] = layout[LastDigitIndex(layout)], layout[layout.index('.')]

print(sum([i*int(x) for i, x in enumerate(layout[:layout.index('.')])]))