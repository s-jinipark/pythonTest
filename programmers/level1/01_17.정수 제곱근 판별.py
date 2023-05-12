def solution(n):
    answer = -1  #0
    for i in range(1, n+1) :  # 반 만 가도 될 듯
        tmp = i * i
        print(tmp, i)
        if n == tmp :
            print(tmp, i)
            answer = (i+1) * (i+1)
            break

    return answer

#n = 121
n = 1

re = solution(n)
print(re)

print("====================")

