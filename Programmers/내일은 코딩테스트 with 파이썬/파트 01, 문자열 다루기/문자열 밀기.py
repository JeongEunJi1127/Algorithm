def solution(A, B):
    answer = 0
    word = []
    for i in range(len(A)):
        word.append(A[len(A)-i:len(A)] + A[:len(A)-i])

    if B in word:
        answer = word.index(B)
    else:
        answer = -1
    return answer