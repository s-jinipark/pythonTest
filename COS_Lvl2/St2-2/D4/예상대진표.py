# 예상대진표

def solution(n,a,b):
    answer = 1

    #코드를 작성하세요.

    print(a//2)
    print(b//2)
    while a != b :
        a = a//2
        b = b//2
        answer += 1

    return answer



n = 8
c = 4 #3
d = 7 #2
res = solution(n,c,d)
print(res)

