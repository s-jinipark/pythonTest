
##### 수들의 합
def solution():
    answer = 0
    for i in range(N-1):  # -1 로 함
        tmp = inp[i]
        if tmp == M:
            print(i,'-', tmp)  # 이부분을 빠뜨렸었음...
            answer += 1
        for j in range(i+1, N):
            #print(i,j)
            tmp  += inp[j]
            if tmp == M :
                print(i, j, tmp)
                answer += 1
                break
    return answer

'''
슬라이딩 윈도우로..
'''

N=8
M=3
inp = [1,2,1,3,1,1,1,2]
re = solution()
print(re)
#=> 5

N=1000
M=100
inp = [4,5,5,3,5,3,1,5,2,1,2,4,5,3,3,1,2,3,2,1,2,2,5,2,1,1,2,1,3,2,1,5,5,4,2,5,2,4,1,1,2,3,4,4,1,2,5,4,4,5,1,5,3,5,3,3,1,4,3,1,1,4,1,3,2,5,5,4,3,2,4,3,2,3,5,3,2,4,2,2,5,4,1,2,5,2,4,3,4,3,4,4,3,3,1,1,1,5,3,4,4,4,5,5,1,2,5,5,5,1,3,5,3,3,5,5,2,4,5,3,5,1,5,1,3,3,5,1,1,4,1,1,3,2,2,4,5,3,2,3,4,1,2,2,5,4,4,2,3,3,3,1,1,4,5,2,2,5,1,4,1,1,5,5,5,1,4,3,3,1,1,3,1,1,5,5,4,4,3,4,5,4,2,3,5,2,3,1,1,1,4,1,2,1,1,1,2,3,3,3,1,2,2,4,4,2,1,5,5,5,2,5,1,5,1,5,2,4,4,2,4,3,2,5,5,1,1,3,3,5,1,4,4,1,5,2,1,1,3,4,2,4,1,4,4,4,1,5,2,3,1,2,3,2,2,1,4,5,2,5,2,3,2,1,5,2,5,1,5,3,4,2,3,5,5,3,4,5,4,5,5,4,4,4,2,3,2,3,3,5,3,5,4,1,5,5,3,5,2,1,1,5,4,2,1,1,3,4,2,5,4,3,1,4,3,4,2,3,3,2,4,1,4,4,5,4,1,4,3,4,1,5,1,3,4,3,5,5,3,1,2,4,5,5,2,2,3,2,5,5,4,2,1,1,2,5,1,5,2,1,2,1,4,1,4,5,5,4,1,3,4,1,5,1,2,5,5,4,3,4,4,5,5,5,4,5,5,5,3,3,1,3,2,2,2,2,1,1,3,1,3,4,4,4,1,4,3,4,1,5,3,5,2,2,3,4,3,5,2,4,4,3,1,5,1,1,1,5,5,2,5,4,4,2,4,4,2,2,1,4,5,1,2,2,2,5,3,2,2,1,4,5,1,1,2,2,1,1,1,2,4,3,4,1,3,1,1,5,5,2,3,3,1,2,2,5,2,1,4,5,5,1,2,4,3,5,5,4,4,4,3,1,1,3,1,4,1,5,1,2,3,5,4,1,1,4,4,1,1,3,4,2,1,1,5,2,3,5,2,5,3,4,3,2,5,3,3,2,5,5,5,2,2,4,4,5,4,2,2,2,5,5,3,3,1,2,3,3,4,2,3,5,5,4,1,2,5,1,4,1,1,3,1,1,3,3,1,3,5,2,4,4,3,5,2,2,3,4,3,2,5,4,5,1,2,4,1,5,1,2,2,2,1,1,1,2,4,4,4,5,2,1,2,4,5,1,4,5,3,3,3,3,5,4,2,2,3,5,1,5,4,5,1,1,1,4,4,2,2,3,3,3,1,3,4,4,4,3,1,1,2,5,4,2,2,4,3,5,5,2,1,5,1,4,3,1,1,3,2,2,5,4,3,3,4,1,4,2,4,1,5,2,5,3,2,4,1,4,5,3,2,2,3,2,2,5,4,4,1,4,3,4,1,4,3,4,5,2,5,4,3,4,3,5,4,5,2,4,2,3,3,1,3,2,3,2,2,2,2,5,1,5,4,5,3,5,2,1,5,5,1,2,3,3,2,2,4,3,1,2,5,5,2,5,2,2,1,4,1,4,4,3,2,5,5,3,2,1,4,3,5,3,5,5,5,1,2,2,3,1,4,3,3,2,1,5,5,5,3,4,1,2,2,3,3,3,4,1,3,5,3,1,3,4,5,3,4,3,1,3,4,1,2,1,2,2,2,4,2,3,3,2,5,2,2,1,4,1,5,2,3,1,3,4,1,4,2,4,3,2,5,1,2,1,3,4,5,4,4,1,5,1,3,3,1,5,3,4,4,2,2,3,3,5,4,5,1,4,5,1,5,4,3,4,2,5,2,4,1,2,5,5,5,5,1,2,2,5,2,1,3,5,2,4,3,5,5,2,1,3,4,5,1,4,4,4,4,2,4,1,5,4,5,2,2,5,3,2,1,1,4,1,1,3,2,2,1,4,5,2,1,2,1,4,2,5,3,4,1,4,4,5,1,2,3,5,4,5,2,2,2,2,5,2,3,4,1,2,2,5,2,2,1,3,5,3,2,1,3,2,3,2,3,2,3,3,5,4,4,3,3,1,2,3,2,5,3,5,5,4,1,3,2,2,1,2,5,3,1,2,3,4,3,5,2,1,3,4,1,4]
re = solution()
print(re)
#=> 312

