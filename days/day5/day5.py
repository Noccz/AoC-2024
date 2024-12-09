import math

def solve(orderingRules, updates, part):
    finalSum = 0
    correctUpdates = []
    wrongUpdates = []
    for update in updates:
        correctSoFar = True
        currentOrder = []
        for item in update:
            #print('---'+item+'---')
            for k in orderingRules:
                if correctSoFar and k != item and k in update and k not in currentOrder:
                    #print(k)
                    #print(orderingRules.get(k))
                    if str(item) in orderingRules.get(k):
                        correctSoFar = False
                        break
            if correctSoFar:
                currentOrder.append(item)            
            
            #print('***** '+str(currentOrder)+' *****')
            #print("")

        if correctSoFar:
            finalSum += int(update[math.floor(len(update)/2)])
        else:
            wrongUpdates.append(update)
    #print("")
    #print(correctUpdates)
    #print(finalSum)
    if part == 1:
        return finalSum
    else:
        return wrongUpdates

def part2(orderingRules, updates):
    wrongUpdates = solve(orderingRules, updates, 2)
    print(wrongUpdates)
    updates = []
    for update in wrongUpdates:
        currentOrder = []
        correctSoFar = False
        while(not correctSoFar):
            correctSoFar = True
            for item in update:
                #print('---'+item+'---')
                for k in orderingRules:
                    if correctSoFar and k != item and k in update and k not in currentOrder:
                        #print(k)
                        #print(orderingRules.get(k))
                        if item not in orderingRules.get(k) and item not in currentOrder:
                            correctSoFar = False
                            currentOrder.append(item)
                #if correctSoFar:
                    #currentOrder.append(item)            
                
                print('***** '+str(currentOrder)+' *****')
                print("")
            if not correctSoFar:
                index = len(currentOrder)-1
                temp = update[index]
                update[index] = update[index+1]
                update[index+1] = temp
        updates.append(update)
        print("---------------------------------")
    return 0

def part1(orderingRules, updates):
    return solve(orderingRules, updates, 1)

def main():
    orderingRules = {}
    updates = []
    section = 1
    with open("exampleInput", "r",) as input:
        while line := input.readline():
            if len(line.strip()) == 0:
                section = 2
                continue
            if section == 1:
                rules = line.strip().split("|")
                orderingRules.setdefault(rules[0], []).append(rules[1])
            if section == 2:
                updateLine = line.rstrip()
                updates.append(updateLine.split(","))
    #print(part1(orderingRules, updates))
    part2(orderingRules, updates)
    return 0

if __name__=="__main__":
    main()