t = int(input())
for _ in range(t):
    a,b = input().split()
    sa = list("".join(a))
    sb = list("".join(b))
    sa.sort()
    sb.sort()

    if sa == sb:
        print(a,"&",b,"are anagrams.")
    else:
        print(a,"&",b,"are NOT anagrams.")