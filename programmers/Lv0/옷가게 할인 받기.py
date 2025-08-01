def solution(price):
    answer = 0
    if price >= 500000:  # 50만원 이상 20% 할인
        answer = price * 0.8  # 1 - 0.2 = 0.8
    elif price >= 300000: # 30만원 이상 10% 할인
        answer = price * 0.9  # 1 - 0.1 = 0.9
    elif price >= 100000: # 10만원 이상 5% 할인
        answer = price * 0.95 # 1 - 0.05 = 0.95
    else:
        answer = price

    return int(answer)
