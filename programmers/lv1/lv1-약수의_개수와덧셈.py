
def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        #print(i)
        print(cnt_measure(i))
        # 짝수 : 더하고 , 홀수 : 뺀다
        tmp = cnt_measure(i)
        if  tmp%2== 0 : # 짝수
            answer += i
        else : # 홀수
            answer -= i
    return answer

def cnt_measure(num) :
    rtn_val = 0
    s = set() # 비어 있는 집합 자료형
    for i in range(1, num):
        #for j in range(i+1, num+1):  # 4*4 = 16 이 빠짐
        for j in range(i, num):  # 4*4 = 16 이 빠짐    
            #print(str(i) + "/" + str(j))
            if num == i * j :
                #rtn_val += 2
                print(str(i) + "/" + str(j))
                s.add(i)
                s.add(j)
    rtn_val = len(s)
    return rtn_val

left	= 1
right   = 2
an = solution(left, right)
print("=====")
print(an)