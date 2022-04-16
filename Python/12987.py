def solution(A, B):
    answer = 0
    A_idx = 0
    B_idx = 0

    A.sort()
    B.sort()

    while B_idx != len(B):
        if A[A_idx] < B[B_idx]:
            answer += 1
            A_idx += 1
            B_idx += 1
        else:
            B_idx += 1

    return answer


# print(solution([2,2,2,2],[1,1,1,1]))
# print(solution([2,2,2,2],[2,2,2,2]))
# print(solution([5,1,3,7],[2,2,6,8]))