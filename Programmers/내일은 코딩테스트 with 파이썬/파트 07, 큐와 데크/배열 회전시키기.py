from collections import deque

def solution(numbers, direction):
    queue = deque()
    if direction == "right":
        queue.appendleft(numbers[-1])
        for i in numbers[0:-1]:
            queue.append(i)
    else:
        k = numbers[0]
        for i in numbers[1:]:
            queue.append(i)
        queue.append(k)
        
    answer = []
    for i in queue:
        answer.append(i)
    return answer