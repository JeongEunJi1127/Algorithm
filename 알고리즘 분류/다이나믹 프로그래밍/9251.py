# LCS 문제 - 최장 공통 부분 수열 구하기
s1 = input()
s2 = input()

# 이중 배열 선언
lcs = [[0] * (len(s2)+1) for _ in range(len(s1)+1)]

for i in range(1,len(s1)+1):
    for j in range(1,len(s2)+1):
        # 문자 하나씩 비교
        # 같으면 이전에 같았던 문자 수 + 1
        if s1[i-1] == s2[j-1]:
            # 기존의 최대 공통 부분수열에 새로 비교한 수를 더한 것이 최대 공통 부분수열
            lcs[i][j] = lcs[i-1][j-1] + 1
        # 문자 다르면
        else:
            # 부분 수열은 연속된 값이 아니므로, 이전의 최대 공통 부분수열은 계속해서 유지되므로
            lcs[i][j] = max(lcs[i-1][j],lcs[i][j-1])

print(lcs[-1][-1])
