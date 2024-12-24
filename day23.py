def find_triangles(computers, connections):
    # Create an adjacency set for the graph
    adjacency = {computer: set() for computer in computers}
    for u, v in connections:
        adjacency[u].add(v)
        adjacency[v].add(u)

    triangles = set()

    # Check for triangles
    for u in computers:
        for v in adjacency[u]:
            if v > u:  # Avoid duplicate checks
                for w in adjacency[v]:
                    if w > v and w in adjacency[u]:
                        # Add the triangle (sorted to avoid duplicates)
                        triangles.add(tuple(sorted([u, v, w])))

    return list(triangles)


computers_set = set()
connections = []

with open("input.txt") as file:
    for line in file.readlines():
        connections.append([x for x in line.removesuffix('\n').split('-')])
        for x in line.removesuffix('\n').split('-'):
            computers_set.add(x)
#connections = [set(x) for x in connections]

computers = list(computers_set)
triangles = find_triangles(computers, connections)
possible_historians = []
for triangle in triangles:
    if any([computer[0] == 't' for computer in triangle]):
        possible_historians.append(triangle)
print(len(possible_historians))