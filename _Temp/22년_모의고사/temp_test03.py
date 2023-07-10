
# 재귀호출 연습_tmp
n = 3 # 주사위 3개
temp = []
cnt = 0

def DFS(v) :
    global cnt
    if v == n :
        print(temp)
        cnt += 1
        return
    else :
        for i in range(1,7):
            temp.append(i)
            DFS(v+1)
            temp.pop()

DFS(0)

print('cnt:', cnt)
print('==============================')
