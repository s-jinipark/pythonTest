def solution(s):
    answer = ''
    lst = list(s.split())
    res = []
    print(lst)
    for l in lst:
        tmp = ''
        for c in range(len(l)):
            print(c)
            if c % 2 == 0 :
                tmp += l[c].upper()
            else:
                tmp += l[c].lower()
        res.append(tmp)
    for i in range(len(res)):
        answer += res[i]
        if i < len(res)-1 :
            answer += ' '
    return answer

s = "try hello world"

re = solution(s)
print(re)

print("====================")

# 아무래도 공백을 다 세주어야 할 듯

def solution2(s):
    answer = ''
    idx = 0
    # 공백이면 0 으로 셋팅
    for i in s :
        print(i)
        if i == ' ':
            idx = 0
            answer += ' '
            continue
        if idx % 2 == 0 : # 짝수
            answer +=  i.upper()
        else :
            answer += i.lower()
        idx += 1

    return answer

re2 = solution2(s)
print(re2)