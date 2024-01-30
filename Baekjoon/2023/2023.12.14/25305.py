n,k = map(int,input().split())

scores = list(map(int,input().split()))
scores.sort(reverse=True)

scores = scores[k-1:]
print(scores[0])