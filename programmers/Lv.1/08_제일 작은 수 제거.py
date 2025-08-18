def solution(arr):
    answer = arr
    min_arr = min(answer)
    answer.remove(min_arr)
    if len(answer) == 0:
        answer.append(-1)
    return answer

