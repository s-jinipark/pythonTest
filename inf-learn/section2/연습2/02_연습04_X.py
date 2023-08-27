
##### 대표값
def solution():
    answer = 0
    # 평균 먼저
    tot = sum(inp)
    avg = round(tot/N)
    print(avg)
    f_cha = 100 # 가장 작은 차이
    f_score = 0 # 그 중 가장 높은 점수
    f_ss = 0  # 그 학생의 순번

    # for i in range(len(inp)):
    #     tmp = inp[i]-avg
    #     #print(tmp) # 절대값이 기억 안남.
    #     if tmp < 0 :
    #         tmp *= -1
    #     print(tmp, inp[i])
    #     if tmp == 0:
    #         f_score = inp[i]
    #         f_ss = i+1
    #         break
    #     if f_cha >= tmp :  # 작거나 같은 경우 후보
    #         f_cha = tmp
    #         if f_score < inp[i]:  # 큰 경우만 넣으면 됨
    #             f_score = inp[i]
    #             f_ss = i+1
    # print("=>", avg, f_score,
    #       f_ss)

    ## [2] 풀이를 보고 해봄
    for idx, val in enumerate(inp):  # 일단 enumerate 쓰는 거
        print(idx, val, abs(val-avg))
        # 평균 과의 차이는 abs (이게 생각 안 났었음)
        tmp = abs(val-avg)
        if f_cha > tmp :  # ** 여기서 작은 경우와 같은 경우로 나눠야 함. 기존에 >= 으로 해서 섞임
            f_cha = tmp  # 가장 작은 차이
            f_score = val  # 그 중 가장 높은 점수
            f_ss = idx  # 그 학생의 순번
        elif f_cha == tmp : # ** 여기서 작은 경우와 같은 경우로 나눠야 함. 기존에 >= 으로 해서 섞임
            if f_score < val :
                f_cha = tmp
                f_score = val
                f_ss = idx
    print("=>", avg, f_score,
          f_ss)
    return answer

N = 10
inp = [45, 73, 66, 87, 92, 67, 75, 79, 75, 80]
re = solution()
print(re)
#=> 74  7

N = 15
inp = [12, 34, 17, 6, 11, 15, 27, 42, 39, 31, 25, 36, 35, 25, 17]
re = solution()
print(re)
#=> 25  11  (난 25 2 가 나옴??)

'''
판박이 - 똑같이 틀림
25 와 같이 차이가 0 일 경우 를 고려해야 한다.. (함정이다.)
'''