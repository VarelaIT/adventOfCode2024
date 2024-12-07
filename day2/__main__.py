def readFile():
    try:
        file = open("input.txt", "r")
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
        return [0, [prev, curr]]
    if not validate(prevDiff) and validate(diff):
        return [1, [curr, next]]
    if not validate(diff) and validate(diffNext):
        return [1, [prev, next]]
    return None

def setDirection(prev, curr):
    if(prev < curr):
        return 1
    if(prev > curr):
        return -1
    return 0

saveReports = 0

for line in inputLines:
    good = True
    bad = 0
    loop = 1
    dir = 0
    diff = 0
    prev = 0
    curr = 0
    numbers = line.split()
    print(numbers)
    while loop < len(numbers):
        curr = int(numbers[loop])
        if(loop == 1):
            prev = int(numbers[0])
            curr = int(numbers[1])
            next = int(numbers[2])
            #print("index: ", loop, "prev: ", prev, "curr: ", curr, "status: ", prev - curr)
            result = compareDiff(prev, curr, next)
            if(result is None):
                good = False
                break
            if(result[0] == 0):
                dir = setDirection(result[1][0], result[1][1])
                prev = curr
                loop += 1
                continue
            if(result[0] == 1):
                bad += 1
                dir = setDirection(result[1][0], result[1][1])
                loop += 2
                prev = result[1][1]
                continue
        #print("index: ", loop, "prev: ", prev, "curr: ", curr, "status: ", prev - curr)
        if(not validate(prev - curr)):
            bad += 1
            loop += 1
            if(bad > 1):
                good = False
                break
            continue
        elif(setDirection(prev, curr) != dir):
            bad += 1
            loop += 1
            if(bad > 1):
                good = False
                break
            continue
        if(bad > 1):
            good = False
            break
        prev = curr
        loop += 1
       
        
    print("Valid: ", good)
    if good == True:
        saveReports += 1 

print("total: ", saveReports)


