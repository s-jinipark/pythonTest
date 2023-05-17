def solution(s):
    answer = True
    tmp = []
    for c in s :
        print(c)
        if c == "(" :
            tmp.append("(")
        else :  # ")" 일 경우 겠지.
            if len(tmp) > 0 and tmp[-1] == "(" :
                tmp.pop()
            else:
                return False
    if len(tmp) > 0 :  # 뭔가 남아 있다?
        return False
    return True


s = "()()"
re = solution(s)
print(re)

s2 = "(())()"
re2 = solution(s2)
print(re2)

s3 = ")()("
re3 = solution(s3)
print(re3)

s4 = "(()("
re4 = solution(s4)
print(re4)
