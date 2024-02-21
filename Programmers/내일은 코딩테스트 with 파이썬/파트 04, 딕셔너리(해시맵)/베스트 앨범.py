def solution(genres, plays):
    answer = []
    dict = {}
    genre_length = {}
    for i in range(len(genres)):
        try:
            dict[genres[i]].append((i,plays[i]))
            genre_length[genres[i]] += plays[i]
        except:
            dict[genres[i]] = [(i,plays[i])]
            genre_length[genres[i]] = plays[i]
            
    genre_length = sorted(genre_length.items(),key = lambda x:x[1],reverse = True)
    for i in genre_length:
        for j in sorted(dict[i[0]],key=lambda x:x[1],reverse = True)[:2]:
            answer.append(j[0])
            
    return answer