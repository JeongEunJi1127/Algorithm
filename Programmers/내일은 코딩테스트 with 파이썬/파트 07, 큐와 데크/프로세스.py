from collections import deque
def solution(priorities, location):
    answer = []
    queue = deque()
    for idx,i in enumerate(priorities):
        queue.append((i,idx))

    while len(queue) > 0:
        tmp = queue.popleft()  

        if max(priorities) > tmp[0]:
            queue.append(tmp)
        else:
            priorities.remove(max(priorities))
            answer.append(tmp[1])
    ans = list(answer).index(location) +1
    return ans