
# 프로그래머스 스타일 로 ...
def solution(name):
    answer = 0

    # A 부터 시작
    # 순방향과 역방향의 차이를 구할 수 있는가
    lt = ord('A')
    rt = ord('Z')
    prev = lt

    for n in name :
        print(  ord(n) ,  ord(n) - lt , rt -ord(n) , min(ord(n) - ord('A'), ord('Z') - ord(n) + 1) )

    return answer

name = "JEROEN"

re = solution(name)
print('re :', re)
#=>
print('==============================')
