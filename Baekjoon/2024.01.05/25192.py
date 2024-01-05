import sys

n = int(sys.stdin.readline())
ans = 0
people = set()
for i in range(n):
    m = sys.stdin.readline().strip()
    if m == "ENTER":
        ans += len(people)
        people.clear()
    else:
        people.add(m)
ans += len(people)
print(ans)