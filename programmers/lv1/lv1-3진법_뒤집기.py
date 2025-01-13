
import math

def solution(n):
    answer = 0

    tmp = n
    tmp_3  = ""
    while tmp > 0 :
        #print( tmp/3 )
        #print( tmp%3 )
        tmp_3 = str(tmp%3) + tmp_3
        tmp = int(tmp/3)
    #print(tmp_3)
    #print(tmp_3[::-1])
    tmp_3 = tmp_3[::-1]
    print(len(tmp_3))
    up = len(tmp_3) -1
    for ch in tmp_3:
        print(ch)
        answer += int(ch) * int( math.pow(3, up) )
        print(up)
        up -=1
    return answer


n = 45
an = solution(n )
print("=====")
print(an)