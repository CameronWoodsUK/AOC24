def Check(update, rules):
    for rule in rules:
        if rule[0] in update and rule[1] in update:
            if update.index(rule[0]) >= update.index(rule[1]):
                return False
        
    return True

def Middle(lst):
    return lst[len(lst)//2]

def Swap(lst, i1, i2):
    lst[i1], lst[i2] = lst[i2], lst[i1]


rules = []
updates = []
with open("input.txt") as file:
    flag = False
    for line in file.readlines():
        if line == '\n':
            flag = True
        elif not flag:
            rules.append([int (x) for x in line.replace('\n', '').split('|')])
        else:
            updates.append([int(x) for x in line.replace('\n', '').split(',')])

count = 0
for update in updates:
    if Check(update, rules):
        count += Middle(update)
print(count)