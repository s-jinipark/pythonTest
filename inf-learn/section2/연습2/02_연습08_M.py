
##### 뒤집은 소수
# 뒤집는 함수인 def reverse(x) 와 소수인지를 확인하는 함수 def isPrime(x)를 반드시 작성

def reverse(x):
    tmp_s = str(x)
    rev_s = ''
    for i in range(len(tmp_s)-1, -1, -1):
        #if tmp_s[i] == '0':  # [2] 우.. 이러면 0 은 무조건 지움
        if tmp_s[i] == '0' and rev_s == '':  # [2]
            continue
        rev_s += tmp_s[i]
    #print( rev_s )
    return rev_s

def isPrime(x):
    for i in range(2, x):
        if x % i == 0 :
            return False
    return True

def solution(N):
    tmp = []
    answer = 0
    for i in inp:
        #print(i)
        #print(reverse(i) )
        rev = reverse(i)
        if int(rev) < 2 :
            continue
        if isPrime(int(rev)):
            tmp.append(rev)
    print(tmp)
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

# 두번 째는 0 무조건 지웠다가
# 고쳤지만 첫번째 결과와 동일
# reverse 해서 1 나오는 경우를 제외 해 줌


