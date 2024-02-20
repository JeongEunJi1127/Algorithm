def solution(id_pw, db):
    answer = ''
    if id_pw in db:
        answer = 'login'
    else:
        if id_pw[0] in [db[i][0] for i in range(len(db))]:
            answer = 'wrong pw'
        else:
            answer = 'fail'
    return answer