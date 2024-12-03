import re

def compute(mul):
    numbers = mul.replace("mul(", "").replace(")", "").split(",")
    return int(numbers[0]) * int(numbers[1])

def part2(memories):
    finalSum = 0
    computeFlag = True
    for memory in memories:
        matches = re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", memory)
        for match in matches:
            if computeFlag and match.startswith("mul"):
                finalSum += compute(match)
            if match.startswith("do()"):
                computeFlag = True
            if match.startswith("don't()"):
                computeFlag = False

    return finalSum

def part1(memories):
    finalSum = 0
    for memory in memories:
        matches = re.findall(r"mul\(\d+,\d+\)", memory)
        for match in matches:
            finalSum += compute(match)

    return finalSum

def main():
    memories = []
    with open("input", "r",) as input:
        while line := input.readline():
            memories.append(line)
    
    print(part1(memories))
    print(part2(memories))

if __name__=="__main__":
    main()