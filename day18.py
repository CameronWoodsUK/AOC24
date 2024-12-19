from collections import deque as DEQ
width, height = 71, 71
def FindPath(map):
    global width, height
    queue = DEQ([[(0,0)]])
    seen = set([(0,0)])
    while queue:
        path = queue.popleft()
        x, y = path[-1]
        if map[y][x] == '*':
            return path
        for x2, y2 in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
            if 0 <= x2 < width and 0 <= y2 < height and map[y2][x2] != "#" and (x2, y2) not in seen:
                queue.append(path + [(x2, y2)])
                seen.add((x2, y2))

def part_2(map):
    global byte_coords
    current_path = FindPath(map)
    fallen_bytes = byte_coords[:12]
    for i in range(1025, len(byte_coords)):
        fallen_bytes.append(byte_coords[i])
        map[fallen_bytes[-1][1]][fallen_bytes[-1][0]] = "#"
        if FindPath(map) == None:
            return(fallen_bytes[-1])

byte_coords = []
with open("input.txt") as file:
    for line in file.readlines():
        line = line.replace('\n', '').split(',')
        byte_coords.append((int(line[0]), int(line[1])))

map = []
for i in range(height):
    line = []
    for j in range(width):
        if (j,i) in byte_coords[:1024]:
            line.append("#")
        else:
            line.append('.')
    map.append(line)



map[-1][-1] = '*'
print(len(FindPath(map))-1)
print(part_2(map))