def isSorted(list):
    return all(int(list[i]) <= int(list[i+1]) for i in range(len(list) - 1)) or all(int(list[i]) >= int(list[i+1]) for i in range(len(list) - 1))

def isReportSafe(report):
    safe = True
    for i in range(len(report)-1):
        if safe:
            levelDifference = abs(int(report[i])-int(report[i+1]))
            if levelDifference > 3 or levelDifference < 1:
                safe = False
    return safe

def part2(reports):
    safeReports = 0
    for report in reports:
        safe = None
        for i in range(len(report)):
            tempReport = report.copy()
            if isSorted(tempReport):
                safe = isReportSafe(tempReport)
            if safe == None or safe == False:
                tempReport.pop(i)
            if (safe == None or safe == False) and isSorted(tempReport):
                safe = isReportSafe(tempReport)
            if safe:
                safeReports += 1
                break
            

    return safeReports

def part1(reports):
    safeReports = 0
    for report in reports:
        safe = True
        if isSorted(report):
            safe = isReportSafe(report)
        else:
            safe = False
        if safe:
            safeReports += 1

    return safeReports

def main():
    reports = []
    with open("input", "r",) as input:
        while line := input.readline():
            reports.append(line.rsplit())
    
    print(part1(reports))
    print(part2(reports))

if __name__=="__main__":
    main()