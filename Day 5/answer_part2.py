
import math


def parse_crates(allCrates, crates):
    #print(crates)
    current = 1
    while current < len(crates):
        if crates[current].isnumeric(): 
            return
        elif crates[current].isalpha():
            temp = math.floor(current/4)
            #print(crates[current])
            #print(temp)
            allCrates[temp].append(crates[current])
        current += 4

def parse_instructions(all_crates, instructions):
    #print(all_crates)
    #print(instructions)

    instructions = instructions.split("move")
    instructions = instructions[1].split("from")
    count,instructions = instructions
    instructions = instructions.split("to")
    start, end = instructions

    count.strip()
    start.strip()
    end.strip()

    count = int(count)
    start = int(start) - 1
    end = int(end) - 1

    
    #print(count)
    #print(len(all_crates))
    temp = all_crates[start][len(all_crates[start]) - count:]
    
    #temp.reverse()
    #print(temp)
    all_crates[start] = all_crates[start][:len(all_crates[start]) - count]
    all_crates[end] = all_crates[end] + temp
    
    #print(all_crates)



f = open("D:\Documents\Advent of Code\Day 5\input.txt", "r")

lines = f.readlines()


count = 0
parsing_crates = True
all_crates = []

first_pass = True


for line in lines:
    #print(ascii(line))
    if first_pass:
        count = int(len(line) / 4)
        #print(count)
        first_pass = False
        for x in range(0,count): all_crates.append([])
        #print(all_crates)
    
    if len(line.strip()) == 0:
        parsing_crates = False
        for each in all_crates:
            each.reverse()
    elif parsing_crates:
        parse_crates(all_crates, line)
    else:
        parse_instructions(all_crates, line)

result = ""
for each in all_crates:
    if each:
        result += each.pop()
    else:
        result += " "

#print(all_crates)
print(result)
f.close()
