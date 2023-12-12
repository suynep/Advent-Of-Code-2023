#!/usr/bin/env python3
import locale

file = open("puzzleInput.txt", 'r')

contents = file.readlines()

check_range = [str(i) for i in range(10)]

length = len(contents)
LENGTH = 141 # length of each row, a fixed thing
             # DON'T CONFUSE THE `length` and `LENGTH`

def extractNum(line, pos):
    """
        Function to Extract Number from a specific line
        (string, which is stored in the `contents` array)

        Works properly Only IFF the char of string in the
        `pos` index is in the set {'1, 2, 3, 4, 5, 6, 7, 8, 9'}
        (logic in this case:
        belongs to check_range)
    """
    retNum = '0'
    while True:
        if line[pos] in check_range:
            retNum += line[pos]
            pos += 1
        else:
            break

    return int(retNum)

def gearFinder(contents):
    for i in range(length):
        check_string = contents[i]
        for j in range(LENGTH):
            if check_string[j] == '*':
                rowChecker(contents, i, j)

def rowChecker(contents, posR, posC): # Short for position
    #POSITION_ROW and POSITION_COLUMN

    if (posR != 0 and posR != length - 1):
        colChecker()

def colChecker(contents, posR, posC, flag=0): # flag: 0 -> middle-row
                                              #       1 -> top-most row
                                              #      -1 -> bottom-most row


    count = 0

    if flag == 0:
        checkR = contents[posR]
        up = contents[posR - 1]
        down = contents[posR + 1]

        for i in range(-1, 2):
            if checkR[posC + i] in check_range
