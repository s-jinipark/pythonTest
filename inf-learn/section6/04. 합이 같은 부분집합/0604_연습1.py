
# self
def DFS(v):
    global  rtn
    if v == N :  # 종료 조건
        print(ch)
        tmp_0 = 0
        tmp_1 = 0
        for i in range(N):
            if ch[i] == 1 :
                tmp_1 += inp[i]
            else :
                tmp_0 += inp[i]
        print('tmp_0 vs tmp_1 : ', tmp_0 , tmp_1)
        if tmp_0 == tmp_1 :
            print('----------')
            rtn = 'YES'

        return
    else:
        ch[v] = 0  # 처음에 이거 없어도 될줄 알았는데,
        # 없으면 1 로 셋팅되고 그대로 간다.
        DFS(v+1)
        ch[v] =1
        # 1 넣은 뒤 던진다
        DFS(v+1)


def solution(N):
    answer = 0

    DFS(0)

    return answer

# N개의 원소로 구성된 자연수 집합이 주어지면, 이 집합을 두 개의 부분집합으로 나누었을 때
# 두 부분집합의 원소의 합이 서로 같은 경우가 존재하면 “YES"를 출력하고,
# 그렇지 않으면 ”NO"를 출력하는 프로그램을 작성하세요.

N = 6
inp = [1,3,5,6,7,10]
#rtn = ''
ch = [0] * N  # 여기는 0 부터 하는 게 나을 듯
rtn = 'NO'

re = solution(N)
print('re :', re)

print(rtn)

