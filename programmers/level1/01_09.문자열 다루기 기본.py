def solution(s):
    answer = False
    len_s = len(s)
    if len_s == 4 or len_s == 6 :
        if s.isnumeric() :
            answer = True
    return answer

s = "a234"

re = solution(s)
print(re)

print("====================")
