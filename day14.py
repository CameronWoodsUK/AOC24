robots = []
with open("input.txt") as file:
    for line in file.readlines():
        robots.append([[int(y) for y in x[2:].split(',')] for x in line.replace('\n', '').split(' ')])

for n in range(5):
    space = [[0] * 11] * 7
    for i, robot in enumerate(robots):
        robots[i][0][0] += (robot[0][0]+robot[1][0])%len(space[0]) - 1
        robots[1][0][1] += (robot[0][1]+robot[1][1])%len(space) - 1

        space[robots[i][0][1]][robots[i][0][0]] += 1