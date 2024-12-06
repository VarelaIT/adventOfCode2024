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

def validate(value):
    if value == 0 or value > 3 or value < -3:
        return False
    return True
    
def compareDiff(prev, curr, next):
    prevDiff = prev - curr
    diff = curr - next
    diffNext  = prev - next
    if validate(prevDiff):
        return 0
    if not validate(prevDiff) and validate(diff):
        return 1
    if not validate(diff) and validate(diffNext):
        return -1
    return None

saveReports = 0

for line in inputLines:
    good = True
    bad = 0
    loop = 0
    dir = 0
    diff = 0
    prev = 0
    curr = 0
    for number in line.split():
        curr = int(number)
        direction = 0
        added = False
        if(loop == 1):
            next = int(number[loop + 1])
            result = compareDiff(prev, curr, next)
            if(result is None):
                good = False
                break
            if(result == 1):
                dir = 0
                bad += 1
                #what are we doing here?

        if loop > 0:
            diff = curr - prev
            if diff > 0 and diff < 4:
                direction = 1
            if diff < 0 and diff > -4:
                direction = -1
            if dir == 0 and bad == 0:
                dir = direction
            if not validate(curr):
                bad += 1
                added = True
            elif loop > 1 and dir != 0 and dir != direction:
                bad += 1
                added = True
            if added == False:
                prev = curr
        else:
            prev = curr
        loop += 1
        #print(loop, " dir: ", dir, " count: ", bad, " diff: ", diff, " prev: ", prev)
        if bad > 1:
            good = False
            break
        
    if good == True:
        saveReports += 1 
    print(good, line)

print("total: ", saveReports)


