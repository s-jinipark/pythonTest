
def solution():
    answer = 0
    tmp = [[0] * 5 for _ in range(N)]
    print(tmp)

    for i in inp :
        print(i)
        # 행->열 형태
        tmp[ i[0]-1 ][ i[1]-1 ] = i[2]   # -1 을 해줘야 된다는
    print(tmp)
    return answer

N = 6   # 정점의 수
K = 9   # 간선의 수
inp = [(1,2,7),(1,3,4),(2,1,2),(2,3,5),(2,5,5),
       (3,4,5),(4,2,2),(4,5,5),(6,4,5)]

re = solution()

print('re :', re)
#=>
print('==============================')
