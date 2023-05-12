def solution(n):
    answer = ''
    half_n = int(n/2)
    chk_even = n % 2
    #chk_nam = n // 2
    print(half_n , chk_even)

    for i in range(half_n):
        print("수박", end='')
        answer += "수박"
    if chk_even != 0 :
        print("수", end='')
        answer += "수"

    return answer

n = 3

re = solution(n)
print(re)

print("====================")

