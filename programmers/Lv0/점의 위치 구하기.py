def solution(keyinput, board):
    key_dic = {
        "left": (-1, 0),
        "right": (1, 0),
        "up": (0, 1),
        "down": (0, -1)
    }

    pc = 0  # -1 0 0  1 2
    py = 0  # 0  0 1  1 1

    answer = [0, 0]
    ps_x = board[0] // 2
    ps_y = board[1] // 2

    for key in keyinput:
        dc, dy = key_dic[key]
        pc = answer[0] + dc
        py = answer[1] + dy
        if -ps_x <= pc <= ps_x and -ps_y <= py <= ps_y:
            answer = [pc, py]

            # print("pc: ", pc , "py: ", py)

    return answer
