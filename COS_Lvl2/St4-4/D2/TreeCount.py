def gcd(a, b) :
    while b != 0 :
        r = a % b
        a = b
        b = r
    return a

def solution(w, h):
    answer = 0
    # 코드를 작성하세요.

    tree_w = w // gcd(w, h)
    tree_h = h // gcd(w, h)
    print('>', tree_w, tree_h)  # w 와 h 가 각각이라구 ?? 문제 헛갈림
    answer = (tree_h *2) + (tree_w *2)

    return answer

'''
일정한 간격을 벌리는 문제
160 -> 약수 구함
180 -> 약수 구함
공통으로 들어 있는 약수 중 가장 큰  
'''

w = 160
h = 180
res = solution(w, h)
print(res)

w = 320
h = 220
res = solution(w, h)
print(res)
