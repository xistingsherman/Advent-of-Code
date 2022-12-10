from collections import deque

f = open("D:\Documents\Advent of Code\Day 10\input.txt", "r")

lines = f.readlines()
register = 1
count = 0
sum = 0
crt = ""
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
        
#queue.append([count,register,line])

result = ""
sprite_position = []
count = 0
while count < len(queue):
    cycle, register, line = queue[count]
    #print(cycle, register)

    if int((cycle - 1)% 40) == 0:
        result += "\n"
    sprite_position = [register-1,register,register+1]

    if ((cycle - 1)%  40) in sprite_position:
        result += "#"
    else: 
        result += "."
    
    count += 1
 
    

print(result)

f.close()