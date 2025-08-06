def solution(s):
    s_dic = {
        "p": 0,
        "y": 0,
    }
    answer = True
    s = s.lower()
    for i in range(len(s)):
        if s[i] in s_dic:
            s_dic[s[i]] += 1

    return s_dic["p"] == s_dic["y"]

    # 'p', 'y'의 개수를 구해서 같으면 True, 다르면 False
    # 아예 없으면 무조건 True
