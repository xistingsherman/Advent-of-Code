from collections import Counter

f = open("D:\Documents\Adent of Code\Day 1\input.txt", "r")

lines = f.readlines()

elf_num = 0

calories = dict()
calories[elf_num] = 0

for line in lines: 
    if line == "\n":
        elf_num += 1
        calories[elf_num] = 0

    else:
        calories[elf_num] += int(line)

k = Counter(calories)

highest = k.most_common(3)

total = 0
for each in highest:
    total += each[1]

print(total)

f.close()