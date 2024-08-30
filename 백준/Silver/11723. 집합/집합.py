from itertools import permutations
import sys
input = sys.stdin.readline

m = int(input())
answer = set()

for _ in range(m):
    s = list(input().split())

    if s[0] == "add":
        answer.add(int(s[1]))
    if s[0] == "remove" and int(s[1]) in answer:
        answer.remove(int(s[1]))
    if s[0] == "check":
        if int(s[1]) in answer:
            print(1)
        else:
            print(0)
    if s[0] == "toggle":
        if int(s[1]) in answer:
            answer.remove(int(s[1]))
        else:
            answer.add(int(s[1]))
    if s[0] == "all":
        answer = {i for i in range(1,21)}
    if s[0] == "empty":
        answer.clear()