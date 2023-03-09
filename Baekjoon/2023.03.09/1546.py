n = int(input())
score = list(map(int, input().split()))
max = max(score)
ans = []

for i in score:
    ans.append((i / max) * 100)

print(sum(ans)/len(ans))