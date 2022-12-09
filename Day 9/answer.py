from collections import deque

f = open("D:\Documents\Advent of Code\Day 9\input.txt", "r")

lines = f.readlines()

all_moves = ""

for line in lines:
    line = line.strip()
    direction, spaces = line.split(" ")
    spaces = int(spaces)
    all_moves += direction*spaces

f.close()

head_visited = []
tail_visited = []

x = 0
y = 0

head_visited.append((x,y))

tail_x = x
tail_y = y
tail_visited.append((tail_x, tail_y))

count = 0
for each in all_moves:
    #map the head, then map the tail.
    if "L" in each:
        x -= 1
    if "R" in each:
        x += 1
    if "U" in each:
        y += 1
    if "D" in each:
        y -= 1
    
    head_visited.append((x,y))
    count += 1
    if (abs(head_visited[count][0] - tail_x) == 1) and (abs(head_visited[count][1] - tail_y) > 1):
        tail_x = head_visited[count-1][0]
        tail_y = head_visited[count-1][1]
    elif (abs(head_visited[count][0] - tail_x) > 1) and (abs(head_visited[count][1] - tail_y) == 1):
        tail_x = head_visited[count-1][0]
        tail_y = head_visited[count-1][1]
    elif abs(head_visited[count][0] - tail_x) > 1:
        tail_x += int((head_visited[count][0] - tail_x)/2)
    elif abs(head_visited[count][1] - tail_y) > 1:
        tail_y += int((head_visited[count][1] - tail_y)/2)
    
    tail_visited.append((tail_x, tail_y))

#print(tail_visited)
#print(len(tail_visited))
tail_visited = set(tail_visited)
print(len(tail_visited))
#print(tail_visited)
    
#result = list(head_visited)
#result.sort()
#print(result)

#print(len(head_visited))
#print(all_moves)