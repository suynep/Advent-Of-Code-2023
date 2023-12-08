#!/usr/bin/env python3


nums = [
        'zero',
        'one',
        'two',
        'three',
        'four',
        'five',
        'six',
        'seven',
        'eight',
        'nine'
        ]

nums_nums = [str(i) for i in range(10)]

#def markX(string, start, end):
#
#    retStr = ''
#    i = 0
#    for c in string:
#        if (i not in range(start, end)):
#            retStr += c
#        else:
#            retStr += 'x'
#        i += 1
#
#    return retStr




def findPair(arr, val):
    for i in range(len(arr)):
        if arr[i][1] == val:
            return arr[i][0]
        else:
            continue

def calcLetters(string):
    arr = []
    for word in nums:
        if word in string:
            posl = string.find(word)
            posr = string.rfind(word)
            if (posl != posr):
                arr.append([nums.index(word), posl])
                arr.append([nums.index(word), posr])
            else:
                arr.append([nums.index(word), posl])
#            string = markX(string, pos, pos + len(word))
#            print(string)
    
    for num in nums_nums:
        if num in string:
            posl = string.find(num)
            posr = string.rfind(num)
            if posl != posr:
                arr.append([nums_nums.index(num), posl])
                arr.append([nums_nums.index(num), posr])
            else:
                arr.append([nums_nums.index(num), posl])
#            string = markX(string, pos, pos + len(num))
#            print(string)

    min_ = min(arr[i][1] for i in range(len(arr)))
    max_ = max(arr[i][1] for i in range(len(arr)))

    [minPos, maxPos] = [findPair(arr, min_), findPair(arr, max_)]

#    print(arr)

    return [minPos, maxPos]


def arrAdd(li):
    return 10 * li[0] + li[1]

file = open("puzzleInput.txt", 'r')

sum_ = 0
for line in file:
    sum_ += arrAdd(calcLetters(line))

print(sum_)
    


