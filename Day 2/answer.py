
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

strategy = {'A':'Y','B':'X','C':'Z'}

#print(strategy)

for line in lines: 
    round = line.split()
    round_pts = 0
    if strategy[round[0]] == 'X':
        round_pts += Points.X.value
        #guaranteed win
        round_pts += 6
    elif strategy[round[0]] == 'Y':
        round_pts += Points.Y.value
        #guaranteed loss
        round_pts += 0
    elif strategy[round[0]] == 'Z':
        round_pts += Points.Z.value
        #guaranteed tie
        round_pts += 3
    
    total += round_pts

print(total)
f.close()