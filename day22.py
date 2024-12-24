def Evolve(n: int, i=2000) -> int:
    for _ in range(i):
        n = (n ^ (n*64)) % 16777216
        n = (n ^ (n//32)) % 16777216
        n = (n ^ (n*2048)) % 16777216

    return n

def part_1(secrets: list) -> int:
    ans = 0
    for secret in secrets:
        ans += Evolve(secret)

    return ans

secrets = []
with open("input.txt") as file:
    for line in file.readlines():
        secrets.append(int(line.removesuffix('\n')))

print(part_1(secrets))