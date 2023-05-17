
# 프로그래머스 스타일 로 ...
def solution(N, s, e, k, nlist):
    answer = 0
    tmp = nlist[s-1:e]  # 주의 앞에 하나 빼줌
    print(tmp)
    tmp.sort()
    answer = tmp[k-1]

    return answer

# N개의 숫자로 이루어진 숫자열이 주어지면 해당 숫자열중에서
# s번째부터 e번째 까지의 수를 오름 차순 정렬했을 때 k번째로
N=6
s=2
e=5
k=3
nlist = [5,2,7,3,8,9]
re = solution(N, s, e, k, nlist)
print(re)
#=> 7

N=15
s=3
e=10
k=3
nlist = [4, 15, 8, 16, 6, 6, 17, 3, 10, 11, 18, 7, 14, 7, 15]
re = solution(N, s, e, k, nlist)
print(re)
#=> 6
