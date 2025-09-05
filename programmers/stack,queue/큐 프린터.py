# 1. 실행 대기 큐(Queue)에서 대기중인 프로세스 하나를 꺼냅니다.
# 2. 큐에 대기중인 프로세스 중 우선순위가 더 높은 프로세스가 있다면 방금 꺼낸 프로세스를 다시 큐에 넣습니다.
# 3. 만약 그런 프로세스가 없다면 방금 꺼낸 프로세스를 실행합니다.
#   3.1 한 번 실행한 프로세스는 다시 큐에 넣지 않고 그대로 종료됩니다.

# 6개의 프로세스 [A, B, C, D, E, F]가 대기 큐에 있고 중요도가
# [1, 1, 9, 1, 1, 1] 이므로 [C, D, E, F, A, B] 순으로 실행됩니다. 따라서 A는 5번째로 실행됩니다.

from collections import deque

def solution(priorities, location):
    answer = 0
    queue = deque()
    for i in range(len(priorities)):
        queue.append([i, priorities[i]])

    while queue:
        cur = queue.popleft()
        has_higher = False
        for q in queue:
            if cur[1] < q[1]:
                has_higher = True
                break
        if has_higher:
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer







