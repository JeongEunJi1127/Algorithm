dict = {}
for _ in range(int(input())):
	c, n = input().split()
	dict[n] = c
print(dict[min(dict.keys())])