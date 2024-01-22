def find_parent(parent,x):
    if parent[x] != x:
        return find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n,m = map(int,input().split())
parent = [i for i in range(n+1)]
edges = []
costs = []

for _ in range(m):
    a,b,c = map(int,input().split())
    # 비용에 따라 오름차순 하기 위해 c를 앞에 둠
    edges.append((c,a,b))

edges.sort()

for edge in edges:
    c,a,b = edge
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        costs.append(c)
costs.remove(max(costs))
print(sum(costs))

