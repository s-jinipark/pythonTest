
# 재귀호출 연습
# 주사위 응용

#n = 3 # 주사위 3개
str='BOTK' # 여기 바뀜
temp = []
cnt = 0

def DFS(v) :
    global cnt
    #if v == n :
    if v == len(str): # 여기 바뀜
        print(temp)
        cnt += 1
        return
    else :
        #for i in range(1,7):
        for i in str: # 여기 바뀜
            temp.append(i)
            DFS(v+1)
            temp.pop()

DFS(0)

print('cnt:', cnt)
print('==============================')
