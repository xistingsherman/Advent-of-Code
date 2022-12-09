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

visited = [[] for i in range(10)]

x = 0
y = 0

for each in visited:
    each.append((x,y))
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

    visited[0].append((x,y))
    count += 1
    for each in range(1,10):
        each_x = visited[each][count-1][0]
        each_y = visited[each][count-1][1]
        if (abs(visited[each-1][count][0] - each_x) == 1) and (abs(visited[each-1][count][1] - each_y) > 1):
            each_x = visited[each-1][count-1][0]
            each_y = visited[each-1][count-1][1]
        elif (abs(visited[each-1][count][0] - each_x) > 1) and (abs(visited[each-1][count][1] - each_y) == 1):
            each_x = visited[each-1][count-1][0]
            each_y = visited[each-1][count-1][1]
        elif abs(visited[each-1][count][0] - each_x) > 1:
            each_x += int((visited[each-1][count][0] - each_x)/2)
        elif abs(visited[each-1][count][1] - each_y) > 1:
            each_y += int((visited[each-1][count][1] - each_y)/2)
        
        visited[each].append((each_x, each_y))

#print(visited[9])
tail_visited = set(visited[9])
print(tail_visited)
print(len(tail_visited))
