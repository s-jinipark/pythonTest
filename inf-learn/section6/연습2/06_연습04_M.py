
##### 합이 같은 부분집합(DFS : 아마존 인터뷰)

# def DFS(v, sum) :
#     global  yn
#     #print(sum)
#     if sum *2 == tot :
#         yn = 'YES'
#         return
#     if v == N:
#         return
#     else:
#         DFS(v+1, sum + inp[v])
#         DFS(v+1, sum)

# 여기는 다시한번
def DFS(v, sum):
    if v == N:  # 0 부터 6번까지 왔다
        #print(sum)
        if sum == (tot -sum) :
            print("YES")
            return
    else:
        DFS(v+1, sum)   # 그냥 가는 애와
        DFS(v+1, sum + inp[v]) # 현재꺼 더한 애

def solution():
    answer = 0
    '''
    앞의 부분 집합과 똑같이 가다가.
    sum 만 chk
    
    1부터 했는데 이상하게 답이 맞았다..
    풀이에는 1부터 시작이 아니라 0 부터 시작.
    '''
    sum = 0
    #DFS(1, sum)
    # [2]
    DFS(0,0)
    print(yn)
    return answer

N = 6

inp = [1, 3, 5, 6, 7, 10]
tot = sum(inp)
yn = 'NO'

re = solution()
print(re)
#=> YES
print('====================')

N = 9
inp = [3, 6, 1, 4, 7, 16, 34, 23, 12]
tot = sum(inp)
yn = 'NO'
re = solution()
print(re)
#=> YES
print('====================')

N = 9
inp = [3, 6, 13, 11, 7, 16, 34, 23, 12]
tot = sum(inp)
yn = 'NO'
re = solution()
print(re)
#=> YES

