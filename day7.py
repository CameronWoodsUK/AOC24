operatorList = ['+', '*']

def FindAllOperatorCombos(operatorList, k):
    output=[]
    n = len(operatorList)
    FindAllOperatorCombosRec(operatorList, '', n, k, output)
    return output
def FindAllOperatorCombosRec(operatorList, prefix, n, k, output):
    if k == 0:
        output.append(prefix)
        return prefix
    for i in range(n):
        newPrefix = prefix + operatorList[i]
        FindAllOperatorCombosRec(operatorList, newPrefix, n, k-1, output)

def FindAllSolutions(values):
    operatorCombos = FindAllOperatorCombos(operatorList, len(values)-1)
    solutions = []
    for combo in operatorCombos:
        solution = values[0]
        for i, operator in enumerate(combo):
            solution = eval(str(solution) + operator + str(values[i+1]))
        solutions.append(solution)
    return solutions


equations = []
with open("input.txt") as file:
    for line in file.readlines():
        equations.append(line.replace('\n', '').split(": "))
for i, equation in enumerate(equations):
    equations[i][0] = int(equation[0])
    equations[i][1] = [int(x) for x in equation[1].split(' ')]

ans = 0
for equation in equations:
    if equation[0] in FindAllSolutions(equation[1]):
        ans += equation[0]

print(ans)