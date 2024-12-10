def FindGuard(map):
    for i, line in enumerate(map):
        for j, c in enumerate(line):
            if c in ['^', '>', 'v', '<']:
                return (i, j)

def MoveGuard(map):
    guardpos = FindGuard(map)
    guardDir = map[guardpos[0]][guardpos[1]]

    match guardDir:
        case '^':
            if guardpos[0] == 0:
                return "END"
            elif map[guardpos[0] - 1][guardpos[1]] == '#':
                map[guardpos[0]][guardpos[1]] = '>'
            else:
                map[guardpos[0]][guardpos[1]] = 'X'
                map[guardpos[0] - 1][guardpos[1]] = '^'
        case '>':
            if guardpos[1] == len(map[0]):
                return "END"
            elif map[guardpos[0]][guardpos[1] + 1] == '#':
                map[guardpos[0]][guardpos[1]] = 'v'
            else:
                map[guardpos[0]][guardpos[1]] = 'X'
                map[guardpos[0]][guardpos[1] + 1] = '>'
        case 'v':
            if guardpos[0] == len(map)-1:
                return "END"
            elif map[guardpos[0] + 1][guardpos[1]] == '#':
                map[guardpos[0]][guardpos[1]] = '<'
            else:
                map[guardpos[0]][guardpos[1]] = 'X'
                map[guardpos[0] + 1][guardpos[1]] = 'v'
        case '<':
            if guardpos[1] == 0:
                return "END"
            elif map[guardpos[0]][guardpos[1] - 1] == '#':
                map[guardpos[0]][guardpos[1]] = '^'
            else:
                map[guardpos[0]][guardpos[1]] = 'X'
                map[guardpos[0]][guardpos[1] - 1] = '<'


map = []
with open("input.txt") as file:
    for line in file.readlines():
        map.append(list(line.replace('\n', '')))

while MoveGuard(map) != "END":
    continue

count = 1
for line in map:
    for c in line:
        if c == 'X':
            count += 1

for line in map:
    for c in line:
        print(c, end='')
    print()
print(count)