# 올바른괄호

def solution(s):
    answer = True
    tmp_list = []
    for s1 in s:
        #print(s1)
        if s1 == '(' :
            tmp_list.append(s1)
        elif s1 == ')' :
            if len(tmp_list) > 0 and tmp_list[0] == '(' :
                tmp_list.pop()
            else :
                answer = False
                break
    return  answer
''' 답은
True
True
False
'''

# def solution(s):
#     answer = True
#     tmp_list = []
#     for p in s:
#         #print(p)
#         if p == ')' :
#             if len(tmp_list)>0 and tmp_list.pop() == '(' :
#                 answer = True
#             else :
#                 return False
#         else :
#             tmp_list.append(p)
#
#     return answer


data = "()()"
res = solution(data)
print(res)
data = "(())()"
res = solution(data)
print(res)

data = ")(()))"

res = solution(data)
print(res)


