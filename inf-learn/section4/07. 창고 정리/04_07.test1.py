
# 프로그래머스 스타일 로 ...
def solution(L, M, inp):
    answer = 0

    #창고 높이 조정은 가장 높은 곳에 상자를 가장 낮은 곳으로 이동하는 것을 말한다.
    # print(inp.index(max(inp)) , max(inp))
    # print(inp.index(min(inp)) , min(inp))

    for i in range(M):
        maxVal = max(inp)
        maxIdx = inp.index(maxVal)
        minVal = min(inp)
        minIdx = inp.index(minVal)
        inp[minIdx] += 1
        inp[maxIdx] -= 1

    print(inp.index(max(inp)) , max(inp))
    print(inp.index(min(inp)) , min(inp))

    answer = max(inp) - min(inp)

    return answer

L = 10   # 창고 가로의 길이
M = 50   # 높이 조정

inp = [69, 42, 68, 76, 40, 87, 14, 65, 76, 81]

re = solution(L, M, inp)
print('re :', re)
#=> 20
print('==============================')

L = 20   # 창고 가로의 길이
M = 150   # 높이 조정

inp = [56,80,91,56,36,97,47,15,12,70,40,71,66,10,12,68,72,38,31,55]

re = solution(L, M, inp)
print('re :', re)
#=> 16
print('==============================')

L = 50
M = 300

inp = [53,33,57,45,59,56,63,78,49,24,24,67,81,71,63,33,63,56,96,59,16,38,50,75,31,43,61,95,92,28,51,59,20,81,74,69,72,84,71,94,70,87,39,46,11,20,38,93,91,65]

re = solution(L, M, inp)
print('re :', re)
#=> 17
print('==============================')