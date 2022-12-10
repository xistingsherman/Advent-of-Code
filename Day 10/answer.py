from collections import deque

f = open("D:\Documents\Advent of Code\Day 10\input.txt", "r")

lines = f.readlines()
register = 1
count = 0
sum = 0

queue = []

for line in lines:
    line = line.strip()

    if "addx" in line:
        count += 1
        temp = line.split(" ")
        queue.append([count, register, line])
        count += 1
        queue.append([count, register, line])
        register += int(temp[1])
    if "noop" in line:
        count += 1
        queue.append([count,register,line])
        
queue.append([count,register,line])

while queue:
    count,register, line = queue.pop()

    if count == 20:
        sum += register*20
        print(count, register*20)
    if count == 60:
        sum += register*60
        print(count, register*60)
    if count == 100:
        sum += register * 100
        print(count, register * 100)
    if count == 140:
        sum += register * 140
        print(count, register * 140)
    if count == 180:
        sum += register*180
        print(count,register*180)
    if count == 220:
        sum += register*220
        print(count,register*220)

    #print(count, register)
print(sum)

f.close()