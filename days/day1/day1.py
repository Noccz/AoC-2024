import csv
def part1(leftList, rightList):
    distances = []

    for i in range(len(leftList)):
        distances.append(abs(leftList[i] - rightList[i]))

    totalDistance = 0
    for distance in distances:
        totalDistance += distance

    return totalDistance

def part2(leftlist, rightList):
    similarityScore = 0
    for i in leftlist:
        nrOfMatches = [index for index in range(len(rightList)) if rightList[index] == i]
        similarityScore += i * len(nrOfMatches)

    return similarityScore


def main():
    leftList = []
    rightList = []
    with open("input", "r",) as input:
        while line := input.readline():
            lineList = line.rsplit()
            leftList.append(int(lineList[0]))
            rightList.append(int(lineList[1]))

    leftList.sort()
    rightList.sort()

    print(part1(leftList, rightList))
    print(part2(leftList, rightList))
    

if __name__=="__main__":
    main()