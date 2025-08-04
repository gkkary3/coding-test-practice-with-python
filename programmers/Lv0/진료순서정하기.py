def solution(emergency):
    answer = []
    soted_emergency = sorted(emergency, reverse=True)

    # print(soted_emergency)
    for num in emergency:
        idx = soted_emergency.index(num) + 1
        answer.append(idx)
    return answer
