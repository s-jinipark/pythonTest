import sys
sys.stdin = open("input.txt", "rt")  # 채점 전 주석 처리
t = int(input())  # 케이스가 몇개 인지..

for i in range(t) :
    #print(i)
    N, s, e, k = map(int, input().split())
    su = list(map(int, input().split()))
    su = su[s-1:e]
    su.sort()  # 오름차순  정렬
    tmp = '#'+ str(i+1)
    print(tmp, su[k-1])
