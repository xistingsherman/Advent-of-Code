

f = open("D:\Documents\Advent of Code\Day 3\input.txt", "r")

lines = f.readlines()

total = 0

group = []
for line in lines: 
    # print(len(group))
    if len(group) == 2:
        group.append(line)
        for x in range(0,len(group[0])):
            temp = group[0][x]
            if temp in group[1] and temp in group[2]:
                # print(temp)
                # print(ord)
                c = ord(temp)

                if c >= 97:
                    total += c - 97 + 1
                else:
                    total += c - 65 + 26 + 1
                break
        # print(total)
        group = []
    else:
        group.append(line)


print(total)
f.close()