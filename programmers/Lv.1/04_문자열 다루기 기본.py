def solution(s):
    if len(s) == 4 or len(s) == 6:
        for i in range(len(s)):
            if s[i].isalpha():  # 또는 not s[i].isdigit()
                return False
        return True
    return False
