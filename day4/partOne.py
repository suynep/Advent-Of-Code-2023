#!/usr/bin/env python3

"""

Let's start by tokenizing the input:
    separate by ':' to obtain only the numbers 
    separate the numbers list by '|' to obtain two lists, 
        1st: lottery values
        2nd: our values

"""

file = open("puzzleInput.txt", 'r')
contents = file.readlines() # list of lines

def tokenize(line):
    split_1 = line.split(':')
    split_2 = split_1[1].split('|')
    lottery_val_str = split_2[0].strip()
    lottery_val = lottery_val_str.split()
    lottery_val = [int(i) for i in lottery_val]

    our_val = split_2[1].strip().split()
    our_val = [int(i) for i in our_val]

    return lottery_val, our_val


def cardValCalc(lottery, our):
    count = 0
    card_val = 0
    for i in our:
        if i in lottery:
            card_val = 2 ** count
            count += 1


    return card_val

def allValCalc(contents):
    net_val = 0
    for i in range(len(contents)):
        lottery_arr, our_arr = tokenize(contents[i])
        card_val = cardValCalc(lottery_arr, our_arr)
        net_val += card_val

    return net_val
        

print(allValCalc(contents))



