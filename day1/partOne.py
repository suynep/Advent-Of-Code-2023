#!/usr/bin/env python3


nums = [i for i in range(0, 10)]


file = open("puzzleInput.txt", 'r')
count = 0


def calcDigits(string):
    retDig = 0
    for ind in string:
        try:
            if int(ind) in nums:
                retDig += int(ind)
                break
        except:
            continue

    for ind in string[::-1]:
        try:
            if int(ind) in nums:
                retDig = retDig * 10 + int(ind)
                break
        except:
            continue

    return retDig

s = 0
for line in file:
    s += calcDigits(line)

print("The sum is: ", s)



            









