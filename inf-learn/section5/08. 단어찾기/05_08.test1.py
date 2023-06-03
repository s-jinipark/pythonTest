
# 프로그래머스 스타일 로 ...
def solution(N, note, write):
    answer = 0

    # 인프런 강좌에서는 dictionary 사용.. (참고 할 것)

    n_set = set(note)
    w_set = set(write)

    print(n_set - w_set)

    return answer

N = 5
note = ['big','good','sky','blue','mouse']
write = ['sky','good','mouse','big']

re = solution(N, note, write)
print('re :', re)
#=>
print('==============================')

