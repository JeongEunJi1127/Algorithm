t = int(input())

def isPalindrome(S):
    return recursion(S,0,len(S)-1)

def recursion(S,l,r):
    global cnt
    cnt+=1
    if l >= r:
        return 1
    elif S[l] != S[r]:
        return 0
    else:
        return recursion(S,l+1,r-1)
    
for _ in range(t):
    s = input()
    global cnt 
    cnt = 0
    print(isPalindrome(s),cnt)

