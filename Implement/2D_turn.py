
graph = []
for i in range(10):
    graph.append([j for j in range(10)])
for i in range(len(graph)):
    print(*graph[i])

# start 는 왼쪽 아래 end 는 오른쪽 위
def false_clock():
    start = [len(graph)-1,0]
    end = [0,len(graph[0])]
    # temp에는 켭쳐질 칸을 미리 저장해둔다
    temp = graph[start[0]][start[1]]
    # 왼쪽 (위에서 아래)
    for i in range(start[0]-end[0]-1,-1,-1):
        graph[i+1][start[1]] = graph[i][start[1]]
        print(graph[i][start[1]],end='')
    print()
    # 위쪽 (오른쪽에서 왼쪽)
    for i in range(start[1]+1,end[1]):
        graph[end[0]][i-1] = graph[end[0]][i]
        print(graph[end[0]][i],end='')
    print()
    # 오른쪽 (아래에서 위)
    for i in range(end[0]+1,start[0]+1):
        graph[i-1][end[1]-1] = graph[i][end[1]-1]
        print(graph[i][end[1]-1],end='')
    print()
    # 아래 (왼쪽에서 오른쪽)
    for i in range(end[1]-2,start[1],-1):
        graph[start[0]][i+1] = graph[start[0]][i]
        print(graph[start[0]][i],end='')
    print()
    print("----------------------------")
    graph[start[0]][start[1]+1] = temp
    for i in range(len(graph)):
        print(*graph[i])

# start 는 왼쪽 아래 end 는 오른쪽 위
def true_clock():
    start = [len(graph)-1,0]
    end = [0,len(graph[0])]
    # temp에는 켭쳐질 칸을 미리 저장해둔다
    temp = graph[start[0]][start[1]]
    print("정방향",temp)
     # 아래 (오른쪽에서 왼쪽)
    for i in range(start[1]+1,end[1]):
        graph[start[0]][i-1] = graph[start[0]][i]
        print(graph[start[0]][i],end='')
    print()
    # 오른쪽 (위에서 아래)
    for i in range(start[0]-1,end[0]-1,-1):
        graph[i+1][end[1]-1] = graph[i][end[1]-1]
        print(graph[i][end[1]-1],end='')
    print()
    # 위쪽 (왼쪽에서 오른쪽)
    for i in range(end[1]-2,start[1]-1,-1):
        graph[end[0]][i+1] = graph[end[0]][i]
        print(graph[end[0]][i],end='')
    print()
    # 왼쪽 (아래에서 위)
    for i in range(end[0]+1,start[0]):
        graph[i-1][start[1]] = graph[i][start[1]]
        print(graph[i][start[1]],end='')
    print()
   
    print("----------------------------")
    graph[start[0]-1][start[1]] = temp
    for i in range(len(graph)):
        print(*graph[i])
false_clock()
true_clock()