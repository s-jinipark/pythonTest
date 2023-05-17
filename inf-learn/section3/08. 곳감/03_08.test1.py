
# 프로그래머스 스타일 로 ...
def solution(N, inp, M, chg):
    answer = 0
    for c in chg:
        print(c)
        # 인덱스를 +/- 하는데 max/min 를 넘으면 순환하도록...
        sign = 1
        if c[1] == 0 :
            sign = -1
        for i in range(N):
            tmp = i + (c[2]*sign)
            if tmp > N-1 :
                tmp = tmp % N
            # if tmp < 0 :
            #     tmp *= -1
            print(i , tmp)
        # 첫번째 시도 , 오른쪽은 되는데, 왼쪽이 안되는 듯...
        '''
        (왼쪽 3)
        0 -3 
        1 -2
        2 -1 (
        3 0
        4 1
        '''
    return answer

N = 5
inp = [
[10,13,10,12,15],
[12,39,30,23,11],
[11,25,50,53,15],
[19,27,29,37,27],
[19,13,30,13,19]
]
M = 3
chg = [  # 첫 : 행번호  , 두 : 방향 (0 : 왼쪽, 1 : 오른쪽), 세 : 회전하는 격자의 수
[2,0,3],  # 행 번호는 1부터 시작...
[5,1,2],
[3,1,4]
]
re = solution(N, inp, M, chg)
print(re)
#=>
print('==============================')
