#!/usr/bin/env python3


file  = open('puzzleInput.txt', 'r')

content = file.readlines()


# cube AMT:
#     red: 12
#     green: 13
#     blue: 14


def tokenize(line):
    idArr = line.strip().split(': ') # this separates the `line` string to game id and game data
    gameArr = idArr[1].split('; ') # fetch each game's individual cube data
    indivArr = [ele.split(', ') for ele in gameArr] # split the per-game strings (eg "3 red"/"5 green") in gameArr as individual data (helpful in extraction later) NOTE: This is a 2d array
    return int(idArr[0].split(' ')[-1]), indivArr

def iterCheck(ID, arr):
    red = 1
    blue = 1
    green = 1

    redVal = 0
    blueVal = 0
    greenVal = 0

    mR = 0
    mB = 0
    mG = 0

    for gameSet in arr:
        for ele in gameSet:
            splitArr = ele.split(' ')
            allEl = [ele.split(' ') for ele in gameSet] # create an array like ['4', 'red', '5', 'blue'] etc.
            allAllEl = []
            for i in range(len(allEl)):
                allAllEl += allEl[i]

#            print(splitArr)

#            print(allAllEl)
            if splitArr[1] in allAllEl:
                if splitArr[1] == 'red':
                    red *= 1
                    if (int(splitArr[0]) >= mR):
                        mR = int(splitArr[0])
                    redVal += int(splitArr[0])
    
                if splitArr[1] == 'blue':
                    blue *= 1
                    blueVal += int(splitArr[0])
                    if (int(splitArr[0]) >= mB):
                        mB = int(splitArr[0])
    
                if splitArr[1] == 'green':
                    green *= 1
                    greenVal += int(splitArr[0])
                    if (int(splitArr[0]) >= mG):
                        mG = int(splitArr[0])
            else:
                continue

#            print(redVal, blueVal, greenVal)

    return mR * mB * mG


POW_SUM = 0
for i in range(len(content)):
    ID, arr = tokenize(content[i])
    tupleVal = iterCheck(ID, arr)
    POW_SUM += tupleVal

print(POW_SUM, ' is the correct ANSWER! WOOOHOOO')

#demo = content[95]
#ID, arr = tokenize(demo)
#print(demo, '\t', iterCheck(ID, arr))
