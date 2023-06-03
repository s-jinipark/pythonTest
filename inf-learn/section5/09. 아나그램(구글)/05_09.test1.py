
# 프로그래머스 스타일 로 ...
def solution(inp1, inp2):
    answer = 'YES'  #0

    inp_d = {}

    for i in inp1 :
        #print(i)
        if i in inp_d :
            inp_d[i] += 1
        else :
            inp_d[i] =1
    print(inp_d)

    for j in inp2:
        if j in inp_d :
            inp_d[j] -= 1
    print(inp_d)

    for k in inp_d :
        print(k, inp_d[k])
        if inp_d[k] > 0 :
            answer = 'NO'
            break
    return answer

inp1 = 'AbaAeCe'
inp2 = 'AbaAeCe'

re = solution(inp1, inp2)
print('re :', re)
#=>
print('==============================')

inp1 = 'ADFHTWXenq'
inp2 = 'AXenqWDFHT'

re = solution(inp1, inp2)
print('re :', re)
#=>
print('==============================')

inp1 = 'ABCDEGHKNOPQRUWXbcdfghikotuwxy'
inp2 = 'XbCdfGhiNoPuwUyABcDEgHKkOtQRxW'

re = solution(inp1, inp2)
print('re :', re)
#=>
print('==============================')

inp1 = 'ABCDqtqtqEFqGHIJKLMNOPQRSTUVWetagdgXYabcdefghijklmnopqrstuwxyz'
inp2 = 'aBcdewrqwtqFghIJklMnOpqrsTuegagaeVxyYAbCDEfGHijKLmNoPQRStUwWXz'

re = solution(inp1, inp2)
print('re :', re)
#=>
print('==============================')