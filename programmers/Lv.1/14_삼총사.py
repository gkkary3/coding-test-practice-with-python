def solution(number):
    counter = 0
    for i in range(len(number)):
        for j in range(i + 1, len(number)):
            for k in range(j + 1, len(number)):
                sum = number[i] + number[j]
                if sum + number[k] == 0:
                    counter += 1
    return counter

# [-2, 3, 0, 2, -5]

# i = 0, j= 1 (j+1)
# 1. -2 + 3  = 1    ,  -1 인 것을 찾으면 됨 있으면 count +1
# 2. -2 + 0 = -2   ,  2  인 것을 찾으면됨 있으면 count +1
# 3. -2 + 2 = 0   , 0 인것을 찾으면됨 있으면 count +1
# ...
# i = 1, j=  2 (j+1)
# 1. 3 + 0 = 3 , -3 인것을 찾으면 count + 1