
##### 조합 구하기
'''
굉장히 중요하다며 강조...
'''
def DFS(L):

    if L == M : # 종착지점
        print(res)
        # 여기서 list 에 들어 있으면 pass ??
        lst.append(res)  # 엥? 마지막 값으로만 도배(?)  => [[4, 3], [4, 3], [4, 3], ... ]
    else:
        for i in range(1, N+1):
            if ch[i] == 0 :
                ch[i] =1
                res[L] = i
                DFS(L+1)
                ch[i] =0

def solution():
    answer = 0
    '''
    1부터 N까지 번호가 적힌 구슬이 있습니다. 이 중 M개를 뽑는 방법의 수를 출력하는 프로그램을 작성하세요.

    2개 뽑는거니까 Level 2 까지.
    구슬 4개니까 4가닥으로 뻗어...
    
    중복허용 X, 한번 나왔던거 x
    => 위 순열구하기(중복없음) 에 추가
    => 나왔던 수 들을 저장해서 맞춰 봄 ??
    '''

    DFS(0)
    print(lst)
    return answer

N = 4  # 구슬의 갯수

M = 2  # 뽑는 갯수

res = [0] * M
ch = [0] * (N+1)  # 구슬 번호로 chk 할려고, +1 함
lst = []

re = solution()
print(re)
#=>
print('====================')

