
# 순열, 조합, 부분집합


# N까지 번호가 적힌 구슬. 중복을 허락하여 M번을 뽑아 일렬로 나열
def DFS(L):
    if L == m :
        print(res)
        return
    else :
        for i in range(1,n+1):
            res[L] = i
            DFS(L+1)

def solution():
    answer = 0

    # 레벨이 m 이고 가지치기가 n ?
    DFS(0)

    return answer

n = 3
m = 2

res = [0] * m   # 결과를 넣을

res = solution()

# 이게 중복 순열

from itertools import product

src = [1,2,3]
res2 = list(product(src, src))
print(res2)


print('====================')

# 1부터 N까지 번호가 적힌 구슬이 있습니다.
# 이 중 M개를 뽑아 일렬로 나열하는 방법을 모두 출력합니다.

def DFS2(L):
    if L == m :
        print(res)
        return
    else :
        for i in range(1, n+1):

            if i in res : continue

            res[L]=i
            DFS2(L+1)
            res[L]=0  # 중요, 이부분 넣어줘야 함

def solution2():
    answer = 0
    DFS2(0)
    return answer

#n = 3
#m = 2
res = [0] * m   # 결과를 넣을
solution2()


from itertools import permutations

src = [1,2,3]

res2 = list(permutations(src, 2))
print(res2)


print('====================')


def DFS3(L, s):
    if L == m:
        print(res)
        return
    else:
        for i in range(s, n+1):
            res[L] = i
            #DFS3(L+1, s+1)
            DFS3(L + 1, i + 1)
            res[L] = 0

def solution3():
    answer = 0
    DFS3(0, 1)   # start 가 하나 더 필요
    return answer

n = 3
m = 2
res = [0] * m   # 결과를 넣을
solution3()


from itertools  import  combinations

#src = [1,2,3]

res2 = list(combinations(src, 2))
print(res2)
