def solution(chicken):
    answer = chicken // 10
    n = chicken // 10 + chicken % 10
    while n >= 10:
        coupon = n // 10
        rest = n % 10
        n = rest + coupon
        answer += coupon
    return answer