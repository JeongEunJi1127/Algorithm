n,m = map(int,input().split()) # N은 행의 개수, M은 열의 개수
ans = []

for _ in range(n):
    card = list(map(int,input().split()))
    ans.append(min(card))
print(max(ans))