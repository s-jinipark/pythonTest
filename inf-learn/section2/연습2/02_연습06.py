
##### 자릿수의 합

# 자릿수의 합을 구하는 함수를 def digit_sum(x)를 꼭 작성해서 프로그래밍
def digit_sum(x):
    # 10으로 나누는거?
    tmp = x
    tot = 0
    while tmp > 0:
        #print(tmp // 10, tmp % 10)
        tot += tmp % 10
        tmp = tmp // 10
    return tot

def solution():
    answer = 0
    maxV = 0
    orgV = 0
    for i in inp:
        #print(i)
        tmp = digit_sum(i)
        if maxV < tmp :
            maxV = tmp
            orgV = i
        #maxV = max(maxV, tmp)
        #print('>', tmp)
    answer = orgV
    return answer

N = 3
inp = [125, 15232, 97]
re = solution()
print( re)
#=> 97


N = 7
inp = [137, 460, 603, 40, 521, 128, 125]
re = solution()
print(re)
#=> 137 (이 번엔 맞게 나옴)


N = 50
inp = [401,100,932,79,822,233,192,18,491,965,34,477,255,948,906,959,528,949,200,138,886,66,535,337,493,154,500,717,336,99,849,390,578,659,853,216,590,417,447,724,507,208,675,377,824,780,708,482,790,127]
re = solution()
print(re)
#=> 959

