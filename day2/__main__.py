def readFile():
    try:
        file = open("testinput.txt", "r")
        lines = file.readlines()
        return lines
    except:
        print("Unable to read file.")

inputLines = readFile()
'''
saveReports = 0

for line in inputLines:
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
        prev = curr
        loop += 1
    if good:
        saveReports += 1 
'''


saveReports = 0

for line in inputLines:
    good = True
    bad = 0
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
                bad += 1
            if dir == 0 and bad == 0:
                dir = direction
        if loop > 1 and dir != 0 and dir != direction:
            bad += 1
        if bad > 1:
            good = False
            break
        prev = curr
        loop += 1
    if good:
        saveReports += 1 

print(saveReports)


