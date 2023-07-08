
##### 숫자만 추출
def solution():
    answer = 0

    '''
    문자와 숫자가 섞여있는 문자열이 주어지면 그 중 숫자만 추출하여 그 순서대로 자연수를 만듭니다. 
    만들어진 자연수와 그 자연수의 약수 개수를 출력합니다.
    '''
    t_str = ''
    for i in inp:
        #print(i)
        #if i.isdecimal() :
        if i.isnumeric():
            #print(i)
            t_str += i
    t_int = int(t_str)
    print(t_int)

    cnt = 0
    for i in range(1,t_int+1):
        if t_int % i == 0:
            cnt += 1
    print(cnt)

    return answer

inp = 'g0en2Ts8eSoft'
re = solution()
print(re)
#=> 28
# 6

inp = 'Akdj0Gk1djADG2SDGkdjf'
re = solution()
print(re)
#=> 12
# 6
