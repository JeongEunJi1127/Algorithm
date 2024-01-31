# int() 안에 input() 다음에 ,를 찍고 숫자를 입력하면 그 진법으로 숫자를 입력 받는다는 것을 의미
# bin()은 2진법을 의미
import sys
input = sys.stdin.readline
print(bin(int(input(), 8))[2:])