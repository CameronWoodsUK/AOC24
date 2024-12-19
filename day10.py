class Node:
    def __init__(self, height, children, coords):
        self.height = height
        self.children = children
        self.coords = coords

class Map:
    def __init__(self, data):
        self.data = [[None for j in data[0]] for i in data]
        for i, row in enumerate(data):
            for j in range(len(row)):
                children = []
                try:
                    if data[i-1][j] == data[i][j] + 1:
                        children.append((i-1, j))
                except:
                    pass
                try:
                    if data[i+1][j] == data[i][j] + 1:
                        children.append((i+1, j))
                except:
                    pass
                try:
                    if data[i][j+1] == data[i][j] + 1:
                        children.append((i, j+1))
                except:
                    pass
                try:
                    if data[i][j-1] == data[i][j] + 1:
                        children.append((i, j-1))
                except:
                    pass
                
                self.data[i][j] = Node(data[i][j], children, (i, j))

    def print(self):
        for line in self.data:
            for node in line:
                print(node.height, end='')
            print()
    
    def paths(self, node: Node):
        '''
        if len(node.children) == 0:
            return
        '''

        if any([len(child.children) != 0 or child.height == 9 for child in [self.data[x[0]][x[1]] for x in node.children]]):
            for child in node.children:
                for path in self.paths(self.data[child[0]][child[1]]):
                    yield [node.coords] + path
        else:
            yield [node.coords]

    def trailHeads(self):
        trailHeads = []
        for row in self.data:
            for node in row:
                if node.height == 0:
                    paths = list(self.paths(node))
                    trailHead = [x for x in paths if len(x) == 10]
                    trailHeads.append(trailHead)
            
        return trailHeads
    
    def printScore(self):
        trailHeads = self.trailHeads()
        print("number of trail heads: " + str(len(trailHeads)))
        score = 0
        
        for i, trailHead in enumerate(trailHeads):
            uniqueRoutes = []
            for route in trailHead:
                if route[-1] not in uniqueRoutes:
                    uniqueRoutes.append(route[-1])
                    print(route)
            score += len(uniqueRoutes)
                
            print(f"trailhead {i+1} score: {len(uniqueRoutes)}\n")

        print("total score: " + str(score))

        
        
    

mapData = []
with open("input.txt") as file:
    for line in file.readlines():
        mapData.append([int(x) if x.isdigit() else x for x in line.replace('\n', '')])

map = Map(mapData)
map.print()
#print(list(map.paths(map.data[0][3])))
map.printScore()
#print(map.trailHeads()[0])