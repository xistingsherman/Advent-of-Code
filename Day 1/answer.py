

f = open("D:\Documents\Adent of Code\Day 1\input.txt", "r")

lines = f.readlines()

elf_num = 0

calories = [0]
max = 0

for line in lines: 
    if line == "\n":
        if calories[elf_num] > calories[max]:
            max = elf_num

        elf_num += 1
        calories.append(0)

    else:
        calories[elf_num] += int(line)

print(calories[max])



f.close()