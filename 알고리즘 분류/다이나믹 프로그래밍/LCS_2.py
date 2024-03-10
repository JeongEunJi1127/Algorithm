# 백준 9252
s1 = input()
s2 = input()

lcs = [[""] * (len(s2)+1) for _ in range(len(s1)+1)]

for i in range(1,len(s1)+1):
    for j in range(1,len(s2)+1):
        if s1[i-1] == s2[j-1]:
            lcs[i][j] = lcs[i-1][j-1] + s1[i-1]
        else:
            if len(lcs[i-1][j]) >= len(lcs[i][j-1]):
                lcs[i][j] = lcs[i-1][j]
            else:
                lcs[i][j] = lcs[i][j-1]

print(len(lcs[-1][-1]))
print(lcs[-1][-1])

