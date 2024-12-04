def checkRight(row, searchWord):
    xmasOccurrences = 0
    for i in range(len(row)-3):
        word = row[i] + row[i+1] + row[i+2] + row[i+3]
        if word == searchWord:
            xmasOccurrences += 1
    return xmasOccurrences

def checkLeft(row, searchWord):
    xmasOccurrences = 0
    for i in range(len(row)-3):
        word = row[i+3] + row[i+2] + row[i+1] + row[i]
        if word == searchWord:
            xmasOccurrences += 1
    return xmasOccurrences

def checkDown(xmasTable, columnIndex, searchWord):
    xmasOccurrences = 0
    for i in range(len(xmasTable)-3):
        word = xmasTable[i][columnIndex] + xmasTable[i+1][columnIndex] + xmasTable[i+2][columnIndex] + xmasTable[i+3][columnIndex]
        if word == searchWord:
            xmasOccurrences += 1
    return xmasOccurrences

def checkUp(xmasTable, columnIndex, searchWord):
    xmasOccurrences = 0
    for i in range(len(xmasTable)-3):
        word = xmasTable[i+3][columnIndex] + xmasTable[i+2][columnIndex] + xmasTable[i+1][columnIndex] + xmasTable[i][columnIndex]
        if word == searchWord:
            xmasOccurrences += 1
    return xmasOccurrences


def checkDownRight(xmasTable, rowIndex, searchWord):
    xmasOccurrences = 0
    for i in range(len(xmasTable[rowIndex])-3):
        if rowIndex < len(xmasTable)-3:
            word = xmasTable[rowIndex][i] + xmasTable[rowIndex+1][i+1] + xmasTable[rowIndex+2][i+2] + xmasTable[rowIndex+3][i+3]
            if word == searchWord:
                xmasOccurrences += 1
    return xmasOccurrences

def checkDownLeft(xmasTable, rowIndex, searchWord):
    xmasOccurrences = 0
    for i in range(len(xmasTable[rowIndex])):
        if i > 2 and rowIndex < len(xmasTable)-3:
            word = xmasTable[rowIndex][i] + xmasTable[rowIndex+1][i-1] + xmasTable[rowIndex+2][i-2] + xmasTable[rowIndex+3][i-3]
            if word == searchWord:
                xmasOccurrences += 1
    return xmasOccurrences

def checkUpRight(xmasTable, rowIndex, searchWord):
    xmasOccurrences = 0
    for i in range(len(xmasTable[rowIndex])-3):
        if rowIndex > 2:
            word = xmasTable[rowIndex][i] + xmasTable[rowIndex-1][i+1] + xmasTable[rowIndex-2][i+2] + xmasTable[rowIndex-3][i+3]
            if word == searchWord:
                xmasOccurrences += 1
    return xmasOccurrences

def checkUpLeft(xmasTable, rowIndex, searchWord):
    xmasOccurrences = 0
    for i in range(len(xmasTable[rowIndex])):
        if i > 2 and rowIndex > 2:
            word = xmasTable[rowIndex][i] + xmasTable[rowIndex-1][i-1] + xmasTable[rowIndex-2][i-2] + xmasTable[rowIndex-3][i-3]
            if word == searchWord:
                xmasOccurrences += 1
    return xmasOccurrences


def checkXMAS(xmasTable, x, y):
    xmasOccurrences = 0
    if (xmasTable[x][y] == "A"):
        if(xmasTable[x-1][y-1] == "M" and xmasTable[x+1][y-1] == "M" and xmasTable[x-1][y+1] == "S" and xmasTable[x+1][y+1] == "S"):
            xmasOccurrences += 1
        if(xmasTable[x-1][y-1] == "S" and xmasTable[x+1][y-1] == "S" and xmasTable[x-1][y+1] == "M" and xmasTable[x+1][y+1] == "M"):
            xmasOccurrences += 1
        if(xmasTable[x-1][y-1] == "M" and xmasTable[x+1][y-1] == "S" and xmasTable[x-1][y+1] == "M" and xmasTable[x+1][y+1] == "S"):
            xmasOccurrences += 1
        if(xmasTable[x-1][y-1] == "S" and xmasTable[x+1][y-1] == "M" and xmasTable[x-1][y+1] == "S" and xmasTable[x+1][y+1] == "M"):
            xmasOccurrences += 1
    return xmasOccurrences


def part2(xmasTable):
    xmasOccurrences = 0
    for x in range(len(xmasTable[0])):
        for y in range(len(xmasTable)):
            if x > 0 and x <len(xmasTable[0])-1 and y > 0 and y < len(xmasTable)-1:
                xmasOccurrences += checkXMAS(xmasTable, x, y)
    return xmasOccurrences

def part1(xmasTable):
    xmasOccurrences = 0
    for index in range(len(xmasTable)):
        xmasOccurrences += checkRight(xmasTable[index], "XMAS")
        xmasOccurrences += checkLeft(xmasTable[index], "XMAS")
        xmasOccurrences += checkDownRight(xmasTable, index, "XMAS")
        xmasOccurrences += checkDownLeft(xmasTable, index, "XMAS")
        xmasOccurrences += checkUpRight(xmasTable, index, "XMAS")
        xmasOccurrences += checkUpLeft(xmasTable, index, "XMAS")
        xmasOccurrences += checkDown(xmasTable, index, "XMAS")
        xmasOccurrences += checkUp(xmasTable, index, "XMAS")
    return xmasOccurrences

def main():
    xmasTable = []
    with open("input", "r",) as input:
        while line := input.readline().strip():
            xmasTable.append(line)
    
    print(part1(xmasTable))
    print(part2(xmasTable))

if __name__=="__main__":
    main()