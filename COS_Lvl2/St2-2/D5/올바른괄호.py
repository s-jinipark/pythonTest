# 올바른괄호

def solution(s):
    answer = True
    tmp_list = []
    for p in s:
        #print(p)
        if p == ')' :
            if len(tmp_list)>0 and tmp_list.pop() == '(' :
                answer = True
            else :
                return False
        else :
            tmp_list.append(p)

    return answer


data = "()()"
res = solution(data)
print(res)
data = "(())()"
res = solution(data)
print(res)

data = ")(()))"

res = solution(data)
print(res)


