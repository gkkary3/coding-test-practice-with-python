def solution(rsp):
    rsp_dic = {
        "2": "0",
        "5": "2",
        "0": "5",
    }

    answer = ''

    rps_list = list(rsp)

    for rps in rps_list:
        answer += rsp_dic[rps]

    return answer