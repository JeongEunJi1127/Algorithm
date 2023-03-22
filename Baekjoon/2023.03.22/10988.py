def is_palindrome(ipt):
    if ipt[::-1] == ipt:
        return True
    else:
        return False
s = input()

if is_palindrome(s):
    print("1")
else:
    print("0")
