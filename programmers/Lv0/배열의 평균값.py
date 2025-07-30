def solution(numbers):
    answer = 0

    for num in numbers:
        answer += num
    return answer / len(numbers)


# 시간 복잡도 O(1)
def solution(numbers):
    return sum(numbers) / len(numbers)
