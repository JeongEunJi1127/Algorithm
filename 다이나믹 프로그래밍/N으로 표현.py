# lv3
def solution(n, number):
    dp = [[] for _ in range(9)]
    #  n의 최솟값이 8보다 크면 리턴하므로 n을 1~9 개 이용하여 나타낼수 있는 수 구하기
    for i in range(1,9):
        setlst = set()
        # 5,55,555같이 이어붙인 값들 
        setlst.add(int(str(n)*i))
        
        # i = 3이면 dp[1]&dp[2], dp[2]&dp[1]의 사칙연산이 dp[3]이 된다
        for j in range(1,i):
            for x in dp[j]:
                for y in dp[i-j]:
                    setlst.add(x+y)
                    setlst.add(x-y)
                    setlst.add(x*y)
                    # 예외처리 분모 0
                    if y != 0:
                        setlst.add(int(x/y))
        
        # 숫자 n i개로 만들 수 있는 수 중 number가 존재하면 리턴 i
        if number in setlst:
            return i
        for k in setlst:
            dp[i].append(k)
    # n이 8개 사용될때까지 number가 발견되지 않으면 -1 리턴
    return -1