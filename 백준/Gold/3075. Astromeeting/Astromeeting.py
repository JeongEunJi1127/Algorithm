import sys
input = sys.stdin.readline

# 플로이드-워셜 알고리즘을 이용한 최단 거리 계산
def floyd_warshall(p, graph):
    # 모든 은하 간 최단 거리 계산
    for k in range(1, p + 1):
        for i in range(1, p + 1):
            for j in range(1, p + 1):
                if graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]

def solution():
    t = int(input())  # 테스트 케이스의 수
    for _ in range(t):
        n, p, q = map(int, input().split())  # n: 사람 수, p: 은하 수, q: 경로 수
        galaxy = [int(input()) for _ in range(n)]  # 사람들의 현재 위치
        graph = [[float('inf')] * (p + 1) for _ in range(p + 1)]  # 거리 그래프 (무한대로 초기화)

        # 자기자신과의 거리는 0
        for i in range(1, p + 1):
            graph[i][i] = 0

        # 은하 간의 경로 정보를 입력받고 그래프에 저장
        for _ in range(q):
            i, j, d = map(int, input().split())
            graph[i][j] = min(graph[i][j], d)
            graph[j][i] = min(graph[j][i], d)

        # 플로이드-워셜 알고리즘으로 모든 은하 간 최단 거리 계산
        floyd_warshall(p, graph)

        # 각 은하에 대해 모든 사람들의 이동 비용을 계산
        answer_galaxy = 0
        answer_cost = float('inf')

        for i in range(1, p + 1):  # i번 은하로의 이동 비용 계산
            cost = 0
            for j in range(n):
                if graph[galaxy[j]][i] == float('inf'):  # 갈 수 없는 경우
                    cost = float('inf')
                    break
                cost += graph[galaxy[j]][i] ** 2  # 비용은 거리의 제곱

            if cost < answer_cost:  # 최소 비용 갱신
                answer_galaxy = i
                answer_cost = cost

        # 결과 출력: 미팅 장소와 최소 비용
        print(answer_galaxy, answer_cost)

solution()
