# lv3
def solution(triangle):
    for i in range(1,len(triangle)):
        for j in range(i+1):
            max_val = 0
            if j-1 >=0:
                max_val = max(max_val,triangle[i][j]+triangle[i-1][j-1])
            if j < i:
                max_val = max(max_val,triangle[i][j]+triangle[i-1][j])
            triangle[i][j] = max_val
    return max(max(triangle))