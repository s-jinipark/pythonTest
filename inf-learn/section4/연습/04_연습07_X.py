
# 창고 정리
def findIndex(x):
    for i in range(len(inp)):
        if inp[i] == x:  # 같은 값이 있다해도 index 앞서는..
            return i

def solution():
    answer = 0

    # 최소/최대값을 파악하고, index 까지 알고 있어야...
    min_val = min(inp)
    max_val = max(inp)
    print(min_val, max_val)
    # index 를 구하는 함수를 만들자
    # 가장 높은 곳에 상자를 가장 낮은 곳으로 이동
    print( findIndex(min_val), findIndex(max_val) )
    # 결국 max 인 값은 -1 해주고, min 인 값은 +1 해준다
    for i in range(L):
        min_val = min(inp)
        max_val = max(inp)
        frm = findIndex(max_val)
        to =  findIndex(min_val)
        inp[frm] -= 1
        inp[to] += 1

    min_val = min(inp)
    max_val = max(inp)
    print(min_val, max_val, max_val-min_val)

    return answer


L= 10   # 창고 가로의 길이

inp = [69, 42, 68, 76, 40, 87, 14, 65, 76, 81]

M = 50  # 높이 조정 횟수

re = solution()
print('re :', re)
#=>
print('==============================')

