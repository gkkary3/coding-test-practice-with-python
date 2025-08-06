# 짝수번쨰는 대문자, 홀수번쨰는 소문자로 바꿔서 리턴
# 문자열 전체 짝/홀수 인덱스가 아니라, 단어 별로 판단

def solution(s):
    answer = ''
    s_split = s.split(' ')

    print(s_split)
    ## 주의 s.split()만 쓸 경우 연속된 공백을 하나로 합칩니다.
    ## try  Hello
    len_ = 0
    for s_ in s_split:
        new_word = ''
        for i in range(len(s_)):
            if i % 2 == 0:
                new_word += s_[i].upper()
            else:
                new_word += s_[i].lower()

        answer += new_word + ' '
    return answer[:-1]

