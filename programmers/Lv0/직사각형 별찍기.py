a, b = map(int, input().strip().split(' '))
start = ''
for i in range(b):
    for j in range(a):
        start += '*'
        if j == a-1:
            start += '\n'
print(start)