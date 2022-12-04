
import http.client

f = open("D:\Documents\Advent of Code\Day 4\input.txt", "r")

lines = f.readlines()



count = 0
for line in lines: 
    listy = set()
    line = line.strip()
    left,right = line.split(',')
    l1,l2 = left.split('-')
    r1,r2 = right.split('-')
    l1 = int(l1)
    l2 = int(l2)
    r1 = int(r1)
    r2 = int(r2)

    for each in range(l1,l2+1):
      listy.add(each)

    for each in range(r1,r2+1):
      if each in listy:
        count += 1
        break


print(count)
f.close()
