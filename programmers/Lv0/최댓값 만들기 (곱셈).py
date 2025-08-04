def solution(numbers):
    numbers.sort()
    return numbers[-1] * numbers[-2]

# numbers.sort(reverse=True) 를 하면 최댓값부터 출력!