# def solution(num_list):
#     answer = []
#     for i in range(len(num_list) -1, -1, -1):
#         answer.append(num_list[i])
#     return answer

# deque에서 appendleft는 항상 왼쪽 부터 append를 하여 역순으로 출력 
# queue를 이용한 방법
from collections import deque
def solution(num_list):
    answer = deque()
    for i in num_list:
        answer.appendleft(i)
    return list(answer)
