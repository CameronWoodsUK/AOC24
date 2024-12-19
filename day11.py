def Blink(stones: list):
    res = []
    for stone in stones:
        if stone == 0:
            res.append(1)
        elif len(str(stone)) % 2 == 0:
            s = str(stone)
            res.append(int(s[:len(s)//2]))
            res.append(int(s[len(s)//2:]))
        else:
            res.append(stone * 2024)
    return(res)

stones = []
with open("input.txt") as file:
    stones = [int(x) for x in file.read().split(' ')]

print("Initial arrangement: ")
print(stones)
blinks = 50
count = 0
for stone in stones:
    subStones = [stone]
    for i in range(blinks):
        subStones = Blink(subStones)
    count += len(subStones)

print(f"number of stones after {blinks} blinks: {len(stones)}")

