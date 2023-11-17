T = int(input())

for test_case in range(1, T + 1):
    nums = list(map(int,input().split()))
    ans = 0.0

    if nums[1]-nums[0] != nums[2]-nums[1]:
        ans = abs((nums[2]+nums[0])/2 - nums[1])

    print("#" + str(test_case), ans)

