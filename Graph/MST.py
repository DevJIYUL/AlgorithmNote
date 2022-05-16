# INPUT
# 3 3
# 1 2 1
# 2 3 2
# 1 3 3
def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]
def union_find(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a <b:
        parent[b] = a
    else:
        parent[a] = b
v,e = map(int,input().split())
parent = [0] * (v+1)
edge = []
result = 0
for i in range(1,v+1):
    parent[i] = i

for _ in range(e):
    a,b,c = map(int,input().split())
    edge.append((c,a,b))

edge.sort()

for e in edge:
    cost,a,b = e
    if find_parent(parent,a) != find_parent(parent,b):
        union_find(parent,a,b)
        result+=cost

print(result)