def solution(numer1, denom1, numer2, denom2):
    answer = []
    tmp11 = tmp12 = tmp21 = tmp22 = 0
    if denom1 > denom2 :
        if denom1 % denom2 == 0 :
            tmp21 = numer2 * (denom1 / denom2 )
            tmp22 = denom2 * (denom1 / denom2 )
            tmp11 = numer1
            tmp12 = denom1
        else:
            tmp21 = numer2 * denom1
            tmp22 = denom2 * denom1
            tmp11 = numer1 * denom2
            tmp12 = denom1 * denom2
    elif denom1 < denom2 :
        if denom2 % denom1 == 0:
            tmp21 = numer2
            tmp22 = denom2
            tmp11 = numer1 * (denom2 / denom1 )
            tmp12 = denom1 * (denom2 / denom1 )
        else:
            tmp21 = numer2 * denom1
            tmp22 = denom2 * denom1
            tmp11 = numer1 * denom2
            tmp12 = denom1 * denom2
    elif denom1 == denom2:
        tmp21 = numer2
        tmp22 = denom2
        tmp11 = numer1
        tmp12 = denom1

    answer.append(int(tmp11 + tmp21))
    answer.append(tmp22)
    return answer

#re = solution(1, 2, 3, 4)
#re = solution(9, 2, 1, 3)
re = solution(1, 3, 9, 2)

print(re)
print("====================")

import math

def solution2(numer1, denom1, numer2, denom2):
    answer = []
    # 큰거 작은거를 구분하고, 공약수를 구하면 될 듯
    #print(math.lcm(denom1, denom2))
    LCM = math.lcm(denom1, denom2)
    tmp1 = LCM / denom1
    tmp2 = LCM / denom2
    numer1 *= tmp1
    denom1 *= tmp1
    numer2 *= tmp2
    denom2 *= tmp2

    answer.append(int(numer1 + numer2))
    answer.append(int(denom1))

    return answer

re2 = solution2(1, 3, 9, 2)
print(re2)