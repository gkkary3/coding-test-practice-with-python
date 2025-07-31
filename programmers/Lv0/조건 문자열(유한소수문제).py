import math


def solution(a, b):
    answer = 0

    gcdResult = math.gcd(a, b)
    b = b // gcdResult

    while b % 2 == 0:
        b = b // 2  # 20//2 =>    b = 10
        #  10//2 =>    b = 5

    while b % 5 == 0:
        b = b // 5  # 5//5 =>     b = 1

    if b == 1:
        return 1
    else:
        return 2

# => 기약분수로 나타내고 분모의 소인수가 2,5 안에 있으면 유한소수 -> 1 반환
# 아니면 2반환

# 22와 11의 최대 공약수