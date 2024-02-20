def solution(cards1, cards2, goal):
    answer = ''
    for i in goal:
        if cards1 and i == cards1[0]:
            cards1.remove(cards1[0])
        elif cards2 and i == cards2[0]:
            cards2.remove(cards2[0])
        else:
            answer = 'No'
            break
    if answer != 'No':
        answer = 'Yes'
    return answer