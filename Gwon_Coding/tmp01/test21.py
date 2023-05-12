
# N과 M (1)
# 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
#   . 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열

# 여기 참조 : https://jiwon-coding.tistory.com/21

#N, M = 3 , 1
N, M = 4 , 2
print(N, M)

s = []

def dfs() :
    if len(s) == M :
        print(s)
        return

    for i in range(1, N+1):
        #print(i)
        if i not in s :  # [1,1] 같은 거 빼겠다
            s.append(i)
            dfs()
            s.pop()     # 이거 없으면 RecursionError

dfs()


#====================

# N과 M (2)
# 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
#   . 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
#   . 고른 수열은 오름차순이어야 한다.
# => [2, 1], [3, 1] 같은 거 제외 하겠다는

print('--------------------')
#N, M = 4 , 2
s = []

def dfs2(st) :
    if len(s) == M :
        print(s)
        return

    for i in range(st, N+1):  # 여기가 1 -> st 로 바뀜
        #print(i)
        if i not in s :
            s.append(i)
            dfs2(i)
            s.pop()     # 이거 없으면 RecursionError

dfs2(1)


#====================

# 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
#   . 1부터 N까지 자연수 중에서 M개를 고른 수열
#   . 같은 수를 여러 번 골라도 된다.
# => 이거는 아무 조건 없는  ..

print('--------------------')
#N, M = 4 , 2
s = []

def dfs3():
    if len(s) == M :  # 중지 조건이라고 볼 수 있음
        print(s)
        return

    for i in range(1, N+1):
        #if i not in s :  # 가지치기 하는 부분이 없어짐
        s.append(i)
        dfs3()
        s.pop()

dfs3()


#====================

# 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
#   . 1부터 N까지 자연수 중에서 M개를 고른 수열
#   . 같은 수를 여러 번 골라도 된다.
#   . 고른 수열은 비내림차순이어야 한다.
#       .. 길이가 K인 수열 A가 A1 ≤ A2 ≤ ... ≤ AK-1 ≤ AK를 만족하면, 비내림차순이라고 한다.
# => 중복있는 오름차순.. 문제 설명이 더 어려움...

print('--------------------')
#N, M = 4 , 2
s = []

def dfs4(st):
    if len(s) == M :
        print(s)
        return
    for i in range(st, N+1):
        # 가지 치기 없으니 if 이거 없음
        s.append(i)
        dfs4(i)
        s.pop()

dfs4(1)

