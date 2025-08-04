# def solution(age):
#     age_dic = {
#         "0" : "a",
#         "1" : "b",
#         "2" : "c",
#         "3" : "d",
#         "4" : "e",
#         "5" : "f",
#         "6" : "g",
#         "7" : "h",
#         "8" : "i",
#         "9" : "j"
#     }
#     answer = ""
#     for str_ in str(age):
#         answer+= age_dic[str_]
#     return answer

# 나이를 알파벳으로 a = 0, b = 1, c = 2 ..., j = 9
# a b c d e f ... j
# 0 1 2 3 4 5 ... 9
# ex) 23 = cd
# ex) 51 = fb


def solution(age):
    alpha_arr = ['a','b','c','d','e','f','g','h','i','j']
    age = str(age)
    answer = ''
    for chr in age:
        answer += alpha_arr[int(chr)]

    return answer