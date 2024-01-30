import sys
input = sys.stdin.readline

n = int(input())
houses = list(map(int,input().split()))
houses.sort()

if n % 2 == 0:
    mid_index = len(houses)//2 - 1
else: 
    mid_index = len(houses)//2 

print(houses[mid_index])
    