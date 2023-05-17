
# 프로그래머스 스타일 로 ...
def digit_sum(x):
    tmp_s = str(x)
    tmp_sum = 0
    for i in range(len(tmp_s)) :
        #print(i)
        tmp_sum += int(tmp_s[i])
    return tmp_sum


def digit_sum2(x):
    tmp_sum = 0
    while x > 0:
        #print(x//10, x%10)
        tmp_sum += (x % 10)
        x = x // 10

    return tmp_sum


def solution(N, su):
    answer = 0
    # str 으로 만들어 자른 후 int 로 변환해서 더한다
    max_val = 0

    for s in su:
        tmp = digit_sum(s)
        if max_val < tmp :
            max_val = tmp
            answer = s

    # 숫자를 10 으로 나누어서 .. 더한다
    for s in su:
        tmp2 = digit_sum2(s)
        print(tmp2)

    return answer


N=3
su= [125, 15232, 97]
re = solution(N, su)
print(re)
#=>

