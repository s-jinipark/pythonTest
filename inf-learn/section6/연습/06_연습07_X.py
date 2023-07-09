
##### 동전교환
def DFS(L, sum):
    global  min_val
    if sum > M:
        return
    if L > min_val:
        return
    if sum == M :
        print(sum, L)
        if min_val > L:
            min_val = L
        return
    else :
        for i in range(N):
            DFS(L+1, sum+inp[i])  # L 이 동전의 갯수...

def solution():
    answer = 0
    '''
    여러 단위의 동전들이 주어져 있을 때 거스름돈을 가장 적은 수의 동전으로 교환??
    각 동전은 무한정 쓸 수 있다
    
    -> 
    레벨로 가다가 stop 하면 안되고, sum 넘어가면 stop 하도록
    그리고, 가지는 동전 수 만큼 뻗고
    res 라고 동전수 만큼 배열 만들어서 뻗을 때마다 sum 을 함
    '''
    # [2] 큰 거 부터 하도록 ...
    inp.sort(reverse=True)

    DFS(0,0)
    print('min_val:', min_val)
    return answer

N = 3  # 동전의 갯수
inp = [1,2,5]
M = 15  # 거슬러 줄 금액
res = [0] * N  # 동전 종료 만큼
sum = 0
min_val = 2147000000

re = solution()
print(re)
#=>
print('====================')

