def solution(numbers, hand):
    answer = ''

    lhand = [1,4,7]
    rhand = [3,6,9]

    keypad = {1: (0, 0), 2: (0, 1), 3: (0, 2),
                4: (1, 0), 5: (1, 1), 6: (1, 2),
                7: (2, 0), 8: (2, 1), 9: (2, 2),
                '*': (3, 0), 0: (3, 1), '#': (3, 2)}

    lft = 0  # 가장 최근 왼손의 위치
    rgt = 0  # 가장 최근 오른손의 위치

    for idx,num in enumerate(numbers):
        print(num)
        print("가장 최근 왼손의 위치", lft)
        print("가장 최근 오른손의 위치", rgt)

        if num in lhand:
            answer += "L"
            lft = numbers[idx]
        elif num in rhand:
            answer += "R"
            rgt = numbers[idx]
        else: # 가운데 열 입력
            l_len = abs(keypad[num][0] - keypad[lft][0]) + abs(keypad[num][1] - keypad[lft][1])
            r_len = abs(keypad[num][0] - keypad[rgt][0]) + abs(keypad[num][1] - keypad[rgt][1])

            if l_len == r_len:
                if hand == "right":
                    answer += "R"
                    rgt = numbers[idx]
                else:
                    answer += "L"
                    lft = numbers[idx]
            elif  l_len > r_len:
                answer += "R"
                rgt = numbers[idx]
            elif  l_len < r_len:
                answer += "L"
                lft = numbers[idx]

        print("answer: ",answer)
        print()

    return answer

print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5],"right"))
# "LRLLLRLLRRL"

# 1. 엄지손가락은 상하좌우 4가지 방향으로만 이동할 수 있으며 키패드 이동 한 칸은 거리로 1에 해당합니다.
# 2. 왼쪽 열의 3개의 숫자 1, 4, 7을 입력할 때는 왼손 엄지손가락을 사용합니다.
# 3. 오른쪽 열의 3개의 숫자 3, 6, 9를 입력할 때는 오른손 엄지손가락을 사용합니다.
# 4. 가운데 열의 4개의 숫자 2, 5, 8, 0을 입력할 때는 두 엄지손가락의 현재 키패드의 위치에서 더 가까운 엄지손가락을 사용합니다.
#   4-1. 만약 두 엄지손가락의 거리가 같다면, 오른손잡이는 오른손 엄지손가락, 왼손잡이는 왼손 엄지손가락을 사용합니다.