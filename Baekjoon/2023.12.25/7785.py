import sys
n = int(sys.stdin.readline())
in_company = {}

for _ in range(n):
    people, k = map(str,sys.stdin.readline().split())
    if k == "enter":
        in_company[people] = k
    elif k == "leave":
        del in_company[people]

print("\n".join(sorted(in_company.keys(), reverse=True)))