def solution(n, k):
    answer = 0
    a = n // 10

    answer = (n * 12000) + ((k - a) * 2000)
    return answer

# 10인분 음료 1개
# 1인분 12,000  음료 2,000
# 총 얼마?? 