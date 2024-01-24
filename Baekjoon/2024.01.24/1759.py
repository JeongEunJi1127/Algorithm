from itertools import combinations

l,c = map(int,input().split())
lst = list(map(str,input().split()))
mo = []
ja = []
for i in lst:
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u" :
        mo.append(i)
    else:
        ja.append(i)

ans = set()
for i in range(1,len(mo)+1):
    comb_mo = []
    for k in list(combinations(mo,i)):
        comb_mo.append("".join(k))

    for j in range(2,len(ja)+1):
        comb_ja = []
        for h in list(combinations(ja,j)):
            comb_ja.append("".join(h))
        if i+j == l:
            for a in range(len(comb_mo)):
                for b in range(len(comb_ja)):
                        final = comb_mo[a] + comb_ja[b]
                        ans.add("".join(sorted(final)))
print(*sorted(ans),sep="\n")