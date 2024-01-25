from bisect import bisect_left, bisect_right

# list에서 start부터 end까지의 원소의 개수 구하는 함수
def count_range(l,start,end):
    return bisect_right(l,end) - bisect_left(l,start)

def solution(words, queries):
    answer = []
    # 단어의 길이는 최대 10000
    d = [[] for _ in range(10001)]
    reversed_d = [[] for _ in range(10001)]

    for word in words:
        d[len(word)].append(word)
        reversed_d[len(word)].append(word[::-1])
    
    for i in range(10001):
        d[i].sort()
        reversed_d[i].sort()
    
    for query in queries:
        if query[0] != "?":
            ans = count_range(d[len(query)], query.replace("?", "a"), query.replace("?","z"))
        else:
            ans =  count_range(reversed_d[len(query)], query[::-1].replace("?", "a"), query[::-1].replace("?","z"))
        answer.append(ans)
    return answer