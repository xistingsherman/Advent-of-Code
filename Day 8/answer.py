
f = open("D:\Documents\Advent of Code\Day 8\input.txt", "r")

lines = f.readlines()

graph = []
transposed_graph = []
result = []

for line in lines:
    line = line.strip()
    graph.append([int(l) for l in line])
    result.append([True for l in line])

transposed_graph =[[graph[j][i]for j in range(len(graph))] for i in range(len(graph[0]))]

# for each in transposed_graph:
#     print(each)
#     print()

#print(transposed_graph)
#print(graph)

visible = 2 * (len(graph) + len(graph[0])) - 4
#print(visible)

total_rows = len(graph) - 1
total_cols = len(graph[0]) - 1
for row in range(1,total_rows):
    for col in range(1, total_cols):
        
        current = graph[row][col]
        #print(row,col,current)
        left_max = max(graph[row][0:col])
        right_max = max(graph[row][col+1:])

        #get list above current, get list below current --> get max
        top_array = transposed_graph[col][0:row]
        top_max = max(top_array)

        #print(row,col,current)
        bottom_array = transposed_graph[col][row+1:]
        #print(bottom_array)
        bottom_max = max(bottom_array)
        
        if (current <= left_max) and (current <= right_max) and (current <= top_max) and (current <= bottom_max):
            result[row][col] = False
        
visible = 0
for each in result:
    visible += each.count(True)
    #print(each)
    #print()

print(visible)
f.close()