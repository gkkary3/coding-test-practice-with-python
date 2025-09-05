from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    wating = deque(truck_weights)
    total_weight = 0
    bridge = deque([0] * bridge_length)

    while wating or total_weight > 0:
        time += 1
        total_weight -= bridge.popleft()

        if wating and total_weight + wating[0] <= weight:
            truck = wating.popleft()
            bridge.append(truck)
            total_weight += truck
        else:
            bridge.append(0)

    return time
