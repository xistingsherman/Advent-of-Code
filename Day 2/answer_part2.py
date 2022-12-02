
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

    if round[1] == 'X':
        #lose
        if round[0] == 'A':
            round_pts += Points.Z.value
        elif round[0] == 'B':
            round_pts += Points.A.value
        elif round[0] == 'C':
            round_pts += Points.B.value
    elif round[1] == 'Y':
        #draw
        round_pts += 3
        if round[0] == 'A':
            round_pts += Points.X.value
        elif round[0] == 'B':
            round_pts += Points.Y.value
        elif round[0] == 'C':
            round_pts += Points.Z.value
    else:
        #win
        round_pts += 6
        if round[0] == 'A':
            round_pts += Points.Y.value
        elif round[0] == 'B':
            round_pts += Points.Z.value
        elif round[0] == 'C':
            round_pts += Points.X.value
    
    total += round_pts

print(total)
f.close()