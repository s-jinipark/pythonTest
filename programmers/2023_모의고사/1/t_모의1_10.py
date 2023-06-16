
def DFS(L, kal, sati):
    global cnt
    if L == len(ingredient) :
        print(kal, sati)
        if kal <= k and sati >= s :
            print('^^^')
            cnt += 1
        return
    else:
        DFS(L+1, kal+ingredient[L][0], sati+ingredient[L][1])
        DFS(L+1, kal, sati)

def solution(ingredient, k, s):
    answer = 0

    DFS(0, 0, 0)

    return answer

# 칼로리 k 이하면서, 만족도 s 이상
k = 200  # 칼로리
s = 20   # 만족도

ingredient =  [[100,5],[200,20],[100,15]]  # [칼로리, 만족도 ]

cnt = 0
solution(ingredient, k, s)

