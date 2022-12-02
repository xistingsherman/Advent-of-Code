
# A = rock
# B - Paper
# C - Scissors

#X is Rock
#Y is Paper
#Z is Scissors

from enum import Enum

class Points(Enum):
    A = 1
    B = 2
    C = 3
    X = 1
    Y = 2
    Z = 3

f = open("D:\Documents\Adent of Code\Day 2\input.txt", "r")

lines = f.readlines()

total = 0
round = []


for line in lines: 
    round = line.split()
    round_pts = 0

    round_pts += Points[round[1]].value

    if (round[0] == 'A' and round[1] == 'Y') or (round[0] == 'B' and round[1] == 'Z') or (round[0] == 'C' and round[1] == 'X'):
        #guaranteed win
        round_pts += 6
    elif (round[0] == 'A' and round[1] == 'Z') or (round[0] == 'B' and round[1] == 'X') or (round[0] == 'C' and round[1] == 'Y'):
        #guaranteed loss
        round_pts += 0
    else:
        #guaranteed tie
        round_pts += 3
    
    #print(round[0], round[1],round_pts)
    total += round_pts

print(total)
f.close()