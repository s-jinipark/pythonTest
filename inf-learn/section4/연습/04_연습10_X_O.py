
# 역수열(그리디)

def findIdx(x, num):
    cnt = 0
    for i in range(len(tmp)):
        if tmp[i] == 0:
            cnt += 1
        else:
            continue

        # if cnt == x :
        #     tmp[i+1] = num+1
        #=> 그냥 +1 해서 넣으면 안됨
        if cnt == x+1 : # 그래서.. 다음 0 값을 찾아서 .. 거기에 넣어 줌
            #tmp[i] = num    # [2]여기서 다같이 안하고 아래에서 하니까 원하던 대로 나옴
            return i

def solution():
    answer = 0

    for i in range(len(inp)):
        print(inp[i], i+1)
        print(findIdx( inp[i], i))
        idx = findIdx( inp[i], i)
        tmp[idx] = i+1    # [2] 여기서 해줌
    print(tmp)
    return answer

# 이 부분은 풀이 보고 
# 현재는 이해 안감

def solution2():
    answer = 0

    for i in range(N):
        for j in range(N):
            if inp[i]==0 and tmp[j] ==0:
                tmp[j] = i+1
                break
            elif tmp[j] == 0:
                inp[i] -= 1
            print('>', inp)
            print(tmp)
    return answer

N= 8

inp = [5, 3, 4, 0, 2, 1, 1, 0]   # 역수열
tmp = [0] * N
re = solution()
print('re :', re)
#=>
print('==============================')
tmp = [0] * N
re2 = solution2()
print('re2 :', re2)