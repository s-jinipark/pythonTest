
##### 자릿수의 합

# 자릿수의 합을 구하는 함수를 def digit_sum(x)를 꼭 작성해서 프로그래밍

def digit_sum(x):
    sum = 0
    while x > 0 :
        #print(x//10, x%10)
        sum += x%10  # 순서도 중요
        x= x // 10

    return  sum

def solution():
    answer = 0
    max_val = 0
    for i in inp:
        #print(i)
        t_sum = digit_sum(i)
        #print(i, '>', t_sum)
        if max_val < t_sum:
            answer = i
            # [2] 자릿수의 합이 같을 경우 입력순으로 먼저인 숫자를 출력
            max_val = t_sum  # 이게 없어서 값이 다르게 나옴

    return answer

N = 3
inp = [125, 15232, 97]
re = solution()
print(re)
#=> 97


N = 7
inp = [137, 460, 603, 40, 521, 128, 125]
re = solution()
print(re)
#=> 137 (X) 처음에 난 125 나옴


N = 50
inp = [401,100,932,79,822,233,192,18,491,965,34,477,255,948,906,959,528,949,200,138,886,66,535,337,493,154,500,717,336,99,849,390,578,659,853,216,590,417,447,724,507,208,675,377,824,780,708,482,790,127]
re = solution()
print(re)
#=> 959

