
# 프로그래머스 스타일 로 ...
def solution(N, M, inp):
    answer = 0
    inp.sort()
    print(inp)
    start = 0
    end = N-1
    # cnt = 0
    while True:
        if start == end :
            print(inp[start], start+1)
            answer = start+1
            break
        else:
            #mid = (end-start)//2
            mid = end - start*2
        print('mid:', mid, inp[mid])
        if M == inp[mid]:
            print(inp[mid], mid+1)
            answer =mid+1
            break
        elif M < inp[mid]:
            end = mid -1
        elif M > inp[mid]:
            start = mid +1
        print(start, end)
        # cnt += 1
    return answer

N = 8
M = 32

inp = [23, 87, 65, 12, 57, 32, 99, 81]


re = solution(N, M,inp)
print('re :', re)
#=> 3
print('==============================')

N = 15
M = 99
inp = [73,32,31,49,94,37,40,62,78,66,27,100,99,29,9]
re = solution(N, M,inp)
print('re :', re)
#=> 14
print('==============================')

N = 30
M = 57
inp = [6,32,38,1,28,76,51,8,98,88,74,60,65,57,97,63,56,99,85,5,13,100,61,36,44,50,62,41,91,9]
re = solution(N, M,inp)
print('re :', re)
#=> 16
print('==============================')

N = 100
M = 55
inp = [23,33,74,4,8,5,6,83,76,89,84,32,44,93,65,42,31,17,60,7,20,29,94,3,30,34,91,38,59,55,68,82,36,9,79,92,69,64,78,63,28,1,72,43,100,25,18,53,58,54,39,51,66,71,97,88,37,24,35,10,15,2,70,52,27,95,85,22,40,47,56,99,50,96,46,49,11,45,26,86,19,98,57,67,13,21,16,80,73,77,41,90,12,48,75,81,87,14,61,62]
re = solution(N, M,inp)
print('re :', re)
#=> 55
print('==============================')
