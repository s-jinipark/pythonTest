
def solution(n):
    answer = 0
    '''
    약수란 어떤 수를 나누어 떨어지게 하는 수를 말하며, 
    1과 자기 자신도 포함합니다. 예를 들어 12의 약수는 1, 2, 3, 4, 6, 12 입니다.
    '''
    tmp = []
    for i in range(1, n+1):
        #print(i)
        if n % i ==0 :
            tmp.append(i)

    print(tmp, sum(tmp))
    answer = sum(tmp)
    return answer


n = 12

an = solution(n)
print('an = ', an)

