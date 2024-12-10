wordsearch = []
with open("input.txt") as file:
    for line in file.readlines():
        wordsearch.append(line.replace('\n', ''))

def Horizontal(line, i, j):
    forwards = line[j:j+4]
    backwards = line[j:j-4:-1]
    print(forwards, backwards, i)
    count = 0
    if forwards == "XMAS":
        count += 1
    if backwards == "SAMX":
        count += 1
    
    return count

def Vertical(wordsearch, i, j):
    count = 0
    up = ''
    down = ''
    if i >= 3:
        up = wordsearch[i][j] + wordsearch[i-1][j] + wordsearch[i-2][j] + wordsearch[i-3][j]
    if i <= len(wordsearch)-4:
        down = wordsearch[i][j] + wordsearch[i+1][j] + wordsearch[i+2][j] + wordsearch[i+3][j]
    
    if up == "XMAS" or up[::-1] == "XMAS":
        count += 1
    if down == "XMAS" or down[::-1] == "XMAS":
        count += 1

    return count

def Diagonal(wordsearch, i, j):
    count = 0
    ur, dr, dl, ul = '', '', '', ''
    if i >= 3 and j <= len(wordsearch[i])-4:
        ur = wordsearch[i][j] + wordsearch[i-1][j+1] + wordsearch[i-2][j+2] + wordsearch[i-3][j+3]
    if i <= len(wordsearch)-4 and j <= len(wordsearch[i])-4:
        dr = wordsearch[i][j] + wordsearch[i+1][j+1] + wordsearch[i+2][j+2] + wordsearch[i+3][j+3]
    if i <= len(wordsearch)-4 and j >= 3:
        dl = wordsearch[i][j] + wordsearch[i+1][j-1] + wordsearch[i+2][j-2] + wordsearch[i+3][j-3]
    if i >= 3 and j >= 3:
        ul = wordsearch[i][j] + wordsearch[i-1][j-1] + wordsearch[i-2][j-2] + wordsearch[i-3][j-3]

    if ur == "XMAS" or ur[::-1] == "XMAS":
        count += 1
    if dr == "XMAS" or ur[::-1] == "XMAS":
        count += 1
    if dl == "XMAS" or ur[::-1] == "XMAS":
        count += 1
    if ul == "XMAS" or ur[::-1] == "XMAS":
        count += 1

    return count
    

count = 0
for i, line in enumerate(wordsearch):
    for j, c in enumerate(line):
        if c == 'X':
            count += Horizontal(line, i, j)
            count += Vertical(wordsearch, i, j)
            count += (Diagonal(wordsearch, i, j))

print(count)