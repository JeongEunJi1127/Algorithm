a,b,v = map(int,input().split())

# x = 올라가는 날 수
# ax - b(x-1) = v
# x = (v-b)/(a-b)

x = (v-b)/(a-b)
if x == int(x):
    print(int(x))
else:
    print(int(x) + 1)