

f = open("D:\Documents\Advent of Code\Day 3\input.txt", "r")

lines = f.readlines()

total = 0

priority = []
for line in lines: 
    count = []
    size = len(line)
    half_size = (int) (size/2)
    
    first_half = line[0:half_size]
    second_half = line[half_size:]

    for c in first_half:
        count.append(c)
    
    for c in second_half:
        if c in count:
            priority.append(c)
            # print(c)
            c = ord(c)
            if c >= 97:
                total += c - 97 + 1
            else:
                total += c - 65 + 26 + 1
            break

print(total)
f.close()