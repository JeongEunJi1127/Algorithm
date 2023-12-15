n,m = map(int,input().split())
dic = {}

for _ in range(n):
    address, password = map(str,input().split())
    dic[address] = password

for _ in range(m):
    add = input() # 찾으려는 주소와 아이디
    print(dic[add])
