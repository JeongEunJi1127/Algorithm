n = int(input())
cnt = 1
dancing_people = set()
dancing_people.add("ChongChong")

for _ in range(n):
    p1,p2 = map(str,input().split())
    if p1 in dancing_people and p2 in dancing_people:
        continue
    elif p1 in dancing_people or p2 in dancing_people:
        cnt +=1
        dancing_people.add(p1)
        dancing_people.add(p2)
print(cnt)
    