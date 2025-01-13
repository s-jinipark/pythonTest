
def solution(s):
    answer = ''
    print(len(s)%2)
    tmp = int(len(s)/2)
    if len(s)%2 == 0 :  #짝수
        answer = s[tmp-1:tmp+1]
    else:
        answer = s[tmp]
    return answer


s = "abcde"
an = solution(s)
print("=====")
print(an)