def solution(array, commands):
    result = []

    for com in commands:
        split_arr = sorted(array[com[0] - 1:com[1]])
        result.append(split_arr[com[2] - 1])

    return result
