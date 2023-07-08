
##### 뒤집은 소수

def reverse(x):
    res = 0
    while x > 0:
        t = x % 10
        res = res * 10 + t
        #print(x, t, res)
        x = x//10
    #print()
    return res

def isPrime(x):
    if x == 1 :  # 이거 중요
        return False
    for i in range(2, x):
        if x % i == 0 :
            return  False
    return True

def solution(N):
    answer = 0
    t_lst = []

    for i in inp:
        tmp = reverse(i)
        if isPrime(tmp):
            print(tmp)

    return answer

# first : prime 판단 시 1 일 경우는 False 로 해주어야 ...
# def isPrime(x):
#     rtn = True
#     if x ==1 : return False  # 이 부분은 풀이에서도 이렇게...
#     for i in range(2, x):
#         if x%i == 0 :
#             rtn = False
#     return  rtn
#
# def solution(N):
#     answer = 0
#     t_lst = []
#     # 뒤집은 후 소수이면 출력
#     for i in inp:
#         연습 = str(i)
#         tmp2 = ''
#         for j in range(len(연습)-1, -1, -1):
#             if int(연습[j]) == 0 : continue
#             tmp2 += str(연습[j])
#         if isPrime(int(tmp2)):
#             t_lst.append(tmp2)
#         #print(tmp2)
#     print(t_lst)
#     return answer

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

