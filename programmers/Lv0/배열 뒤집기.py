# def solution(num_list):
#     answer = []
#     for i in range(len(num_list) -1, -1, -1):
#         answer.append(num_list[i])
#     return answer

# queue를 이용한 방법
from collections import deque
def solution(num_list):
    answer = deque()
    for i in num_list:
        answer.appendleft(i)
    return list(answer)
