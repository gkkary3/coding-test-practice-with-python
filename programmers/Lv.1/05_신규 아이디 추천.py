import re
# 아이디의 길이는 3자 이상 15자 이하
# 아이디는 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.) 문자만 사용할 수 있습니다.
# 단, 마침표(.)는 처음과 끝에 사용할 수 없으며 또한 연속으로 사용할 수 없습니다.
def solution(new_id):
    new_id_low = ''
    print('new_id: ', new_id)
    # 1단계
    for id in new_id:
        if id.isalpha():
            new_id_low += id.lower()
        else:
            new_id_low += id
    print('1단계: ', new_id_low)
    # 2단계
    new_id_low = re.sub(r'[^a-z0-9\-_.]', '', new_id_low)
    print('2단계: ', new_id_low)

    # 3단계
    new_id_low = re.sub(r'\.+', '.', new_id_low)
    print('3단계: ', new_id_low)

    # 4단계
    if new_id_low[0] == '.' or new_id_low[-1] == '.':
        new_id_low = dotRemove(new_id_low)

    # 간단한 방법(.strip('.'))
    # : 문자열 양쪽 끝에 있는 마침표만 제거
    print('4단계: ', new_id_low)

    # 5단계
    if new_id_low == "":
        new_id_low = 'a'
    print("5단계: ", len(new_id_low))
    # 6단계
    print("len: ", new_id_low)
    if len(new_id_low) >= 16:
        new_id_low = new_id_low[:15]
        print("split_new_id: ", new_id_low)
        if new_id_low[0] == '.' or new_id_low[-1] == '.':
            new_id_low = dotRemove(new_id_low)
    print("6단계: ", new_id_low)
    # 7단계
    if len(new_id_low) <= 2:
        while len(new_id_low) < 3:
            new_id_low =  new_id_low + new_id_low[-1]
    print("7단계: ", new_id_low)
    return new_id_low

def dotRemove(new_id):
    if len(new_id) > 0 and new_id[0] == '.':
        new_id = new_id[1:]
    print('dotRemove: ', new_id)
    if len(new_id) > 0 and new_id[-1] == '.':
        new_id = new_id[:-1]
    return new_id

# print(solution("...!@BaT#*..y.abcdefghijklm"))
# print(solution("z-+.^."))
# print(solution("=.="))
print(solution("abcdefghijklmn.p"))

# 1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
# 2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
# 3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
# 4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
# 5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
# 6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
#      만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
# 7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.

