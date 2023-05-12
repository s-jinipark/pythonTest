def solution(left, right):
    answer = 0

    for i in range(left, right+1):
        print (i)
        print('>', cnt_yaksu(i))
        if cnt_yaksu(i) % 2 == 0 :
            answer += i
        else :
            answer -= i
    return answer

def cnt_yaksu(n):
    rtn = 0
    for i in range(1, n+1):
        print(i)
        if n%i == 0 :
            rtn += 1
    return rtn

#left = 13
#right = 17

left = 24
right = 27

re = solution(left, right)
print(re)


'''
[기존]

def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        #print(i)
        #print(cnt_measure(i))
        # 짝수 : 더하고 , 홀수 : 뺀다
        tmp = cnt_measure(i)
        if  tmp%2== 0 : # 짝수
            answer += i
        else :
            answer -= i
    return answer

#def cnt_measure(num) :
    # rtn_val = 0
    # s = set() # 비어 있는 집합 자료형
    # for i in range(1, num+1):
    #     #for j in range(i+1, num+1):  # 4*4 = 16 이 빠짐
    #     for j in range(i, num):     
    #         #print(str(i) + "/" + str(j))
    #         if num == i * j :
    #             #rtn_val += 2
    #             #print(str(i) + "/" + str(j))
    #             s.add(i)
    #             s.add(j)
    # rtn_val = len(s)
    # return rtn_val
    
def cnt_measure(number) :
    nums = []
    c = int(number ** 0.5)
    for i in range(1, c+1) :
        if number % i == 0 :
            if i == number//i :
                nums.append(i)
            else :
                nums.append(i)
                nums.append(number//i)

    return len(nums)
'''
