import math

def solution(num1, num2):
    # trunc 사용( 단순히 소수 점 버림)
    # answer = math.trunc(num1/num2 * 1000)

    # floor 사용
    answer = math.floor(num1 / num2 * 1000)

    return answer

print(solution(3,2))
print(solution(7,3))
print(solution(1,16))