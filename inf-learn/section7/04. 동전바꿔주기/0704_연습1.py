
# self
def DFS(L, sum):
    if sum> T:
        return
    if L == k :
        if sum == T:
            print(sum)
        return
    else:
        p, n = inp[L]
        for i in range(n+1):  # oops! 여기가 n+1 ㅠ.ㅠ
            DFS(L+1, sum+(p*i))

def solution():
    answer = 0

    DFS(0, 0)

    return answer

#  금액 T(0<T≤10,000),  동전의 가지 수k(0<k≤10),
T = 20
k = 3
# 동전의금액 pi(0<pi≤T)와 개수 ni(0<ni≤10)
inp = [
    [5, 3],
    [10, 2],
    [1, 5]
]

re = solution()
print('re :', re)

'''
D(L, sum) 스타일이며,
 L 은 동전의 종류

동전의 개수가 있어서
가지를 어떻게 뻗나? (상태트리 어떻게?)
ex) 5 원 0,1,2,3 으로 가지 뻗는다
5*0, 5*1, 5*2, ...
그다음 3가닥으로 뻗는다
10원 0,1,2
'''
