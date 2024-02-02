def solution(friends, gifts):
    answer = {}
    # 행은 주는애, 열은 받는애로 저장
    presents = [[0 for _ in range(len(friends))] for _ in range(len(friends))]
    index = {}

    for i in range(len(friends)):
        index[friends[i]] = i
        answer[friends[i]] = 0

    for gift in gifts:
        # a는 주고 b는 받음
        a, b = gift.split()
        a_index = index[a]
        b_index = index[b]
        # a가 주는 사람
        presents[a_index][b_index] += 1

    # print(presents)

    # 선물 지수 구하기
    get_presents = {}
    give_presents = {}
    gift_rate = {}

    for friend in friends:
        get_presents[friend] = 0
        give_presents[friend] = 0

    for gift in gifts:
        a, b = gift.split()
        get_presents[b] += 1
        give_presents[a] += 1

    for friend in friends:
        gift_rate[friend] = give_presents.get(friend) - get_presents.get(friend)

    # print(gift_rate)

    for i in range(len(friends)):
        giver = list(index.keys())[i]
        for j in range(i, len(friends)):
            getter = list(index.keys())[j]
            p1 = presents[i][j]
            p2 = presents[j][i]

            if p1 > p2:
                answer[giver] += 1
            elif p2 > p1:
                answer[getter] += 1
            # 선물을 주고받은 적이 없거나 같은 수로 선물을 주고받았을 때
            elif (p1 == 0 and p2 == 0) or (p1 == p2):
                p1_rate = gift_rate.get(giver)
                p2_rate = gift_rate.get(getter)
                if p1_rate > p2_rate:
                    answer[giver] += 1
                elif p1_rate < p2_rate:
                    answer[getter] += 1
    # print(answer, answer.values())
    return max(answer.values())