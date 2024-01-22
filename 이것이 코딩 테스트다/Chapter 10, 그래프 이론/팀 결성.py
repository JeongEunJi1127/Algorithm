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
for _ in range(m):
    k,a,b = map(int,input().split())
    if k == 0:
        # 팀 합치기 연산
        union_parent(parent,a,b)
    elif k == 1:
        # 같은 팀 여부 연산
        if find_parent(parent,a) == find_parent(parent,b):
            print("YES")
        else:
            print("NO")