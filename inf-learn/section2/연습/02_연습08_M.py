
##### 뒤집은 소수
def isPrime(x):
    rtn = True
    for i in range(2, x):
        if x%i == 0 :
            rtn = False
    return  rtn

def solution(N):
    answer = 0
    t_lst = []
    # 뒤집은 후 소수이면 출력
    for i in inp:
        tmp = str(i)
        tmp2 = ''
        for j in range(len(tmp)-1, -1, -1):
            if int(tmp[j]) == 0 : continue
            tmp2 += str(tmp[j])
        if isPrime(int(tmp2)):
            t_lst.append(tmp2)
        #print(tmp2)
    print(t_lst)
    return answer

N = 5
inp = [32, 55, 62, 3700, 250]
re = solution(N)
print(re)
#=> ['23', '73']

N = 36
inp = [590,7628,27139,431,73,5652,11890,460,76,3452,2067,902,12,614,18039,518,71,5329,26422,793,41,8808,2878,10,720,49,2808,22122,611,91,8561,27991,408,54,4926,1395 ]
re = solution(N)
print(re)
#=> 37 9811 67 2543 17 397 19
# 오우 난 1 이 들어 감

