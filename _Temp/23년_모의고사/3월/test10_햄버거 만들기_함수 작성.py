
def DFS(v, kal, sati) :
    global  cnt
    if v == n:  # 종료
        print(kal, sati)
        #칼로리가 k이하이면서 만족도가 s이상이 되도록 햄버거를 만드는 방법의 수
        if kal <= k and sati >= s :
            print('>', kal, sati)
            cnt += 1
    else :
        DFS(v + 1, kal+ingredient[v][0], sati+ingredient[v][1])
        DFS(v + 1, kal , sati)

def solution(ingredient, k, s):
    answer = 0

    '''
    다 해봐야 하니 일단 DFS
    레벨은 ingredient 개수
    상태 트리는 사용하냐 or 안하냐..
    '''
    print(n)
    DFS(0, 0, 0)

    answer = cnt
    return answer


ingredient = [[100, 5], [200, 20], [100, 15]] # [칼로리, 만족도] 형태
k = 200
s = 20
# 칼로리가 k이하이면서 만족도가 s이상이 되도록 햄버거를 만드는 방법의 수
n = len(ingredient)
#ch = [0] * (n+1)
cnt = 0

an = solution(ingredient, k, s)

print(an)