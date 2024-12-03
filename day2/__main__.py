def readFile():
    try:
        file = open("input.txt", "r")
        lines = file.readlines()
    except:
        print("Unable to read file.")
    return lines

inputLines = readFile()
reports = []
saveReports = 0
for line in inputLines:
    report = []
    good = True
    loop = 0
    dir = 1
    diff = 0
    prev = 0
    curr = 0
    for number in line.split():
        curr = int(number)
        if loop > 0:
            diff = curr - prev
            if diff > 0 and diff < 4:
                direction = 1
            if diff < 0 and diff > -4:
                direction = 0
            if diff == 0 or diff > 3 or diff < -3:
                good = False
                break
        if loop == 1:
            dir = direction
        if loop > 1 and dir != direction:
            good = False
            break
        report.append(curr)
        prev = curr
        loop += 1
    if good:
        saveReports += 1 
    reports.append(report)



print(saveReports)


