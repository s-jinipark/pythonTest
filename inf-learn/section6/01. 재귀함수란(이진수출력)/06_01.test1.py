
def DFS(x):

    if x == 0 :
        return
    else:
        #print(x // 2, x % 2)
        DFS(x // 2)
        print( x % 2 , end=' ')

    # if x > 0 :
    #     #print(x // 2, x % 2)
    #     DFS(x // 2)
    #     print(x // 2, x % 2)

'''
[계산 과정]
  11 
    5 (11/2) : 1
    2 (5/2) : 1
    1 (2/2) : 0
'''

def solution(N):
    answer = 0

    DFS(N)

    return answer

N = 11

re = solution(N)
print('re :', re)
#=>
print('==============================')
