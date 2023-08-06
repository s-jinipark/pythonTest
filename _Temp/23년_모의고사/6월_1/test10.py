
def solution(a, b):
    answer = 0

    # 1항과 2항은 1, 3항부터는 앞 두항의 합
    tmp = [0] * (b+1)

    tmp[1] = 1
    tmp[2] = 1
    for i in range(3, b+1):
        tmp[i] = tmp[i-1] + tmp[i-2]
    print(tmp)
    for j in range(a, b+1):
        answer += tmp[j]

    return answer

a = 2
b = 5

re = solution(a, b)
print(re)