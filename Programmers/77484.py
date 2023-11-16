def solution(lottos, win_nums):
    answer = []
    win_min = 0
    win_max = 0
    lot = {6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6}

    for lotto in lottos:
        if lotto in win_nums:
            win_min += 1
        elif lotto == 0:
            win_max += 1

    win_max += win_min
    answer.append(lot[win_max])
    answer.append(lot[win_min])

    return answer



print(solution([44, 1, 0, 0, 31, 25],[31, 10, 45, 1, 6, 19]))