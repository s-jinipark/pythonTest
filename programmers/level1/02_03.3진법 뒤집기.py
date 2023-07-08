
def solution(n):
    answer = 0

    # 10 진법을 3 진법으로..
    tmp = n
    n3 = ''
    while tmp > 0 :
        print(tmp % 3, tmp // 3)
        n3 = str(tmp % 3) + n3
        tmp = tmp // 3
    print(n3)
    n3_re = ''
    for i in range(len(n3)-1,-1,-1):
        print(n3[i])
        n3_re += n3[i]
    print(n3_re)

    # 다시 3진법 -> 10 진법으로으로..
    for j in range(len(n3_re)):
        #print(n3_re[j])
        print( int(n3_re[j]) *  (3 ** (len(n3_re)-1-j) ) )
        answer += int(n3_re[j]) *  (3 ** (len(n3_re)-1-j) )
    return answer

n = 45

re = solution(n)
print(re)


'''
[기존]

import math

def solution(n):
    answer = 0
    연습 = n
    tmp_3  = ""
    while 연습 > 0 :
        #print( 연습/3 )
        #print( 연습%3 )
        tmp_3 = str(연습%3) + tmp_3
        연습 = int(연습/3)
    #print(tmp_3)
    #print(tmp_3[::-1])
    tmp_3 = tmp_3[::-1]
    #print(len(tmp_3))
    up = len(tmp_3) -1
    for ch in tmp_3:
        #print(ch)
        answer += int(ch) * int( math.pow(3, up) )
        #print(up)
        up -=1
    return answer
'''