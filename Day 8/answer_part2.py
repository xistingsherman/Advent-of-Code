
f = open("D:\Documents\Advent of Code\Day 8\input.txt", "r")

lines = f.readlines()

graph = []
transposed_graph = []
result = []

for line in lines:
    line = line.strip()
    graph.append([int(l) for l in line])
    result.append([0 for l in line])

transposed_graph =[[graph[j][i]for j in range(len(graph))] for i in range(len(graph[0]))]

total_rows = len(graph) - 1
total_cols = len(graph[0]) - 1
for row in range(1,total_rows):
    for col in range(1, total_cols):
        
        current = graph[row][col]

        left_max = max(graph[row][0:col])
        right_max = max(graph[row][col+1:])
        
        top_array = transposed_graph[col][0:row]
        top_max = max(top_array)

        bottom_array = transposed_graph[col][row+1:]
        bottom_max = max(bottom_array)

        left_score = 0
        right_score = 0
        top_score = 0
        bottom_score = 0
        scenic_score = 0

        #evaluate left
        if current > left_max:
            left_score = col
        else:
            y = col - 1
            while current > graph[row][y] and y > 0:
                y -= 1
            left_score = col - y
        
        #evaluate right
        if current > right_max:
            right_score = len(graph[0]) - col - 1
        else:
            y = col + 1
            while y < len(graph) and current > graph[row][y]: #greater than or equal to?
                y += 1
            right_score = y - col

        #evaluate upper
        if current > top_max:
            top_score = row
        else:
            x = row - 1
            while current > graph[x][col] and x > 0:
                x -= 1
            top_score = row - x
        
        #evaluate lower
        if current > bottom_max:
            bottom_score = len(graph) - row - 1
        else:
            x = row + 1
            while  x < len(graph) and current > graph[x][col]:
                x += 1
            bottom_score = x - row
        
        scenic_score = left_score * right_score * top_score * bottom_score
        result[row][col] = scenic_score

        #print(left_score, right_score, top_score, bottom_score, scenic_score)
        #print()
        
maximum = 0
for each in result:
    #print(max(each))
    maximum = max(max(each),maximum)
    #print(each)


print(maximum)
#print(len(graph))
#print(len(graph[0]))
f.close()