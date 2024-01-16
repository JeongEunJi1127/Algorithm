# LCS (longest common subsequence) 최대 공통 부분 수열 문제
import sys
input = sys.stdin.readline

a = [""]+list(input().rstrip())
b = [""]+list(input().rstrip())
lcs = [[""]*len(b) for _ in range(len(a))]

for i in range(1,len(a)):
    for j in range(1,len(b)):
        if a[i] == b[j]:
            lcs[i][j] = lcs[i-1][j-1] + a[i]
        else:
            if len(lcs[i-1][j]) >= len(lcs[i][j-1]):
                lcs[i][j] = lcs[i-1][j]
            else:
                lcs[i][j] = lcs[i][j-1]
print(len(lcs[-1][-1]))
print(lcs[-1][-1])