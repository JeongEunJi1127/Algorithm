pos = input()

row = int(pos[1]) # 행은 input의 숫자부분
column = int(ord(pos[0])) - int(ord('a')) + 1 # 아스키코드 사용하여 열 구현

# 나이트가 이동할 수 있는 방향
steps = [(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)]

cnt = 0
for step in steps:
    # 이동하고자 하는 위치 확인
    next_row = row + step[0]
    next_column = column + step[1]
    # 해당 위치로 이동 가능하면 카운트 증가
    if next_row >= 1 and next_column >= 1 and next_column <= 8 and next_row <= 8:
        cnt+=1

print(cnt)