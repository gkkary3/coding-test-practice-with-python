def solution(array):
    for i in range(len(array)):
        min_idx = i
        for j in range(i + 1, len(array)):
            if array[min_idx] > array[j]:
                min_idx = j
        array[min_idx], array[i] = array[i], array[min_idx]

    mid_idx = len(array) // 2

    return array[mid_idx]

# sort함수 사용
def solution(array):
    array.sort()
    mid_idx = len(array) // 2
    return array[mid_idx]