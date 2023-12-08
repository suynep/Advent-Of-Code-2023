#!/usr/bin/env python3

file = open("puzzleInput.txt", 'r')

charArr = []
charC = 0
checkR = [str(i) for i in range(0, 10)]

def extractNum(line, pos):
    retNum = '0'
    ppos = pos
    while True:
        if pos < len(line) and line[pos] in checkR:
            if ppos != 0 and line[ppos - 1] not in checkR:
                retNum += line[pos]
                pos += 1
            elif ppos == 0:
                retNum += line[pos]
                pos += 1
            else:

                break
        else:
            break

    return int(retNum)



for line in file:
    charArr.append(line.strip())
    charC += 1

def iterateSolve(arr):
    allNumsArr = []
    s = 0
    for l in range(len(arr)):
        liStr = arr[l]
        for i in range(len(liStr)):
            if (liStr[i]) in checkR:
                num = extractNum(liStr, i)
                if num != 0:
                    allNumsArr.append(num)
                    boolVal = checkPart(l, arr, num, i)
                    if boolVal:
                        s += num

            else:
                continue

    return s
     
def checkPart(l, arr, num, pos):
    length = len(arr)
    numlen = len(str(num))
    if (l != 0 and l != length - 1):
        for x in range(-1, 2):
            if (pos != 0 and pos + numlen - 1 != len(arr[l]) - 1):
                for i in range(-1, numlen + 1):
                    if arr[l + x][pos + i] not in checkR and arr[l + x][pos + i] != '.':
                        return True
            elif pos == 0:
                for i in range(numlen + 1):
                    if arr[l + x][pos + i] not in checkR and arr[l + x][pos + i] != '.':
                        return True
            elif pos + numlen - 1 == length - 1:
                for i in range(-1, 0):
                    if arr[l + x][pos + i] not in checkR and arr[l + x][pos + i] != '.':
                        return True

    elif (l == 0):
        for x in range(0, 2):
            if (pos != 0 and pos + numlen != len(arr[l]) - 1):
                for i in range(-1, numlen + 1):
                    if arr[l + x][pos + i] not in checkR and arr[l + x][pos + i] != '.':
                        return True
            elif pos == 0:
                for i in range(numlen + 1):
                    if arr[l + x][pos + i] not in checkR and arr[l + x][pos + i] != '.':
                        return True
            elif pos +numlen - 1 == length - 1:
                for i in range(-1, 0):
                    if arr[l + x][pos + i] not in checkR and arr[l + x][pos + i] != '.':
                        return True

    elif (l == length - 1):
        for x in range(-1, 1):
            if (pos != 0 and pos + numlen != len(arr[l]) - 1):
                for i in range(-1, numlen + 1):
                    if arr[l + x][pos + i] not in checkR and arr[l + x][pos + i] != '.':
                        return True
            elif pos == 0:
                for i in range(numlen + 1):
                    if arr[l + x][pos + i] not in checkR and arr[l + x][pos + i] != '.':
                        return True
            elif pos + numlen- 1== length - 1:
                for i in range(-1, 0):
                    if arr[l + x][pos + i] not in checkR and arr[l + x][pos + i] != '.':
                        return True

    return False


print(iterateSolve(charArr))
