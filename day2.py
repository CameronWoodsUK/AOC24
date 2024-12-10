def SafeIncrease(report):
    safeChanges = [-1, -2, -3]
    for i in range(1, len(report)):
        dif = report[i-1] - report[i]
        if dif not in safeChanges:
            return False
    return True

def SafeDecrease(report):
    safeChanges = [1, 2, 3]
    for i in range(1, len(report)):
        dif = report[i-1] - report[i]
        if dif not in safeChanges:
            return False
    return True

def DoubleCheck(report):
    combos = []
    for i in range(len(report)):
        combos.append(report[:i] + report[i+1:])

    for combo in combos:
        if SafeDecrease(combo) or SafeIncrease(combo):
            return True
    return False


reports = []
with open("input.txt") as file:
    for line in file.readlines():
        data = line.replace('\n', '').split(' ')
        for i in range(len(data)):
            data[i] = int(data[i])
        reports.append(data)

safeCount = 0
for report in reports:
    if SafeDecrease(report) or SafeIncrease(report) or DoubleCheck(report):
        safeCount += 1
print(safeCount)
