def solution(n):
    answer = 0
    cnt = 1
    while True:
        if ( n * cnt ) % 6 == 0 :
            answer = int(( n * cnt )/ 6)
            break
        else :
            cnt += 1

    return answer


#n = 6
n = 10
re = solution(n)

print(re)
print("====================")

