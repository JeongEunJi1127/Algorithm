n = int(input())

def num(nn):
    ans = 1
    while nn>0:
        ans *= nn
        nn-=1
    return ans
print(num(n))