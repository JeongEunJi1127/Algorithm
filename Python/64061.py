from pprint import pprint

def solution(board, moves):
    answer = 0
    sol = []

    # pprint(board)

    for move in moves:  # moves = [1,5,3,5,1,2,1,4]
        for i in range(len(board)):
            # print(board[i][move-1])
            if board[i][move-1] != 0:
                sol.append(board[i][move-1])
                board[i][move-1] = 0
                pprint(board)
                # print(sol)
                # print(answer)

                if len(sol) >= 2:
                    if sol[-1] == sol[-2]:
                        answer+=2
                        sol.pop()
                        sol.pop()

                break

    return answer

# stack, deque 사용해보기!
print(solution(([0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]),[1,5,3,5,1,2,1,4]) )


