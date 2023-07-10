
# 재귀호출 연습_tmp
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
        # 이부분을 index 로 좀 바꿈
        for i in range(len(str)):
            # [2] 추가 조건
            # B 와 T 가 붙어 있는 경우는 탐색하지 않겠다
            if v > 0 :
                if temp[v - 1] == 'B' and str[i] == 'T' : continue
                if temp[v - 1] == 'T' and str[i] == 'B' : continue

            temp.append(str[i])
            DFS(v+1)
            temp.pop()

DFS(0)

print('cnt:', cnt)
print('==============================')
