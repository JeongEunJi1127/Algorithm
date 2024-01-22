from collections import deque
import copy
n = int(input())
# 진입차수
indegree = [0 for _ in range(n+1)]
# 강의 별 시간
time = [0 for _ in range(n+1)]
# 그래프 
graph = [[] for _ in range(n+1)]

for i in range(1,n+1):
    data = list(map(int,input().split()))
    time[i] = data[0]
    for j in data[1:-1]:
        indegree[i] += 1
        graph[j].append(i) 

def topology_sort():
    q = deque()
    # 그냥 result = time 했더니 오류
    result = copy.deepcopy(time)

    for i in range(1,n+1):
        if indegree[i] == 0:
            q.append(i)

    # 큐가 빌 때까지
    while q:
        now = q.popleft()
        for i in graph[now]:
            # 여러 개의 강의 동시에 들을 수 있으므로 각 i 별로 result[now] + time[i]를 계산해 가장 긴 강의 시간으로 result를 갱신한다
            result[i] = max(result[i],result[now] + time[i])
            # graph[now]와 연결된 노드들의 indegree -= 1 해준다
            indegree[i] -= 1
            # 진입 차수가 0이 되면 큐에 삽입
            if indegree[i] == 0:
                q.append(i)
    for i in range(1,n+1):
        print(result[i])

topology_sort()
