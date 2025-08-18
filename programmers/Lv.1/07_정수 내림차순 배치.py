def solution(n):
    answer = list(str(n))
    sorted_answer = sorted(answer, reverse=True)
    return int("".join(sorted_answer))
