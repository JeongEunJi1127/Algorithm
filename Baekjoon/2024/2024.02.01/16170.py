import time
s = time.strftime('%Y-%m-%d', time.localtime(time.time()))
lst = s.split("-")
for i in lst:
    print(i)