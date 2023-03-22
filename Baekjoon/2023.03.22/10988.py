def is_palindrome(ipt):
    i = len(ipt) // 2
    if len(ipt) % 2 != 0:  
        j = ipt[0:i]
        if j[::-1] == ipt[i+1:len(ipt)]:
            return True
        else:
            return False
    else:
        j = ipt[0:i-1]
        if j[::-1] == ipt[i+1:len(ipt)]:
            return True
        else:
            return False
    
s = input()

if is_palindrome(s):
    print("1")
else:
    print("0")
