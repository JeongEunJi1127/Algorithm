import sys
n,m = map(int,sys.stdin.readline().split())
dict = {}

for _ in range(n):
    word = sys.stdin.readline().strip()

    if len(word) >= m and word not in dict:
        dict[word] = 1
    elif word in dict:
        dict[word] += 1
# 람다 함수에서 정렬 기준들의 오름차순 내림차순 설정을 각각 다르게 하는 법
# => 기준 값 앞에 마이너스 (-)를 붙여 해당 기준만 내림차순으로 정렬
dict = sorted(dict.items(),key = lambda item : (-item[1],-len(item[0]),item[0]))

for i in dict:
    print(i[0])