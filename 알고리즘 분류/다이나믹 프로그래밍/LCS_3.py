# 백준 1958 - 3개의 LCS 구하기
s1 = input()
s2 = input()
s3 = input()

# 아이디어 - 한꺼번에 세는건 아닌 것같고,, 두개의 최장공통부분수열 구한 후 그걸로 다시 한번? -> lcs 함수화
# 땡,, 그냥 3중 포문으로 돌리면 되는거였다! 

lcs = [[[0] * (len(s3)+1) for _ in range(len(s2)+1)]for _ in range(len(s1)+1)]

for i in range(1,len(s1)+1):
    for j in range(1,len(s2)+1):
        for k in range(1,len(s3)+1):
            if s1[i-1] == s2[j-1] and s2[j-1]== s3[k-1]:
                lcs[i][j][k] = lcs[i-1][j-1][k-1] + 1
            else:
                lcs[i][j][k] = max(lcs[i-1][j][k],lcs[i][j-1][k],lcs[i][j][k-1])

print(lcs[-1][-1][-1])

