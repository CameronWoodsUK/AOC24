def calculate_heights(schematic):
    res = [-1 for _ in schematic[0]]
    for row in schematic:
        for i, item in enumerate(row):
            if item == '#':
                res[i] += 1

    return res

def check(key, lock):
    max = 6
    for k, l in zip(key, lock):
        if k + l >= 6:
            return False        
    return True

def count_matches(keys, locks):
    count = 0
    for key in keys:
        for lock in locks:
            if check(key, lock):
                count += 1
    
    return count

with open("input.txt") as file:
    input = [x.split('\n') for x in file.read().split('\n\n')]

key_schematics = []
lock_schematics = []
for item in input:
    if item[0] == '#####' and item[-1] == '.....':
        lock_schematics.append(item)
    if item[0] == '.....' and item[-1] == '#####':
        key_schematics.append(item)

key_heights = [calculate_heights(x) for x in key_schematics]
lock_heights = [calculate_heights(x) for x in lock_schematics]


print(count_matches(key_heights, lock_heights))