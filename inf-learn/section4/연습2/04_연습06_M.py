
# 씨름 선수(그리디)
def solution(n, inp):
    answer = 0
    inp.sort()
    print(inp)
    cnt = 0
    for i in range(len(inp)):
        for j in range(i+1, len(inp)):
            print(i, j)
            if inp[i][1]  > inp[j][1]:
                cnt += 1
                break
    print(cnt)

    print('==========')

    inp.sort(reverse=True)
    print(inp)
    largest = 0
    cnt = 0
    for x, y in inp:
        if y > largest :
            cnt += 1
            largest = y
    print(cnt)

    return answer

'''
키로 소팅하고 뒤에 오는 인원 검사해서.. 몸무게 적은 사람 있으면 cnt

[강사] 이중 for 문은 비효율적이라며...
키로 desc 소트 하고 largest 몸무게가 나올때마다 count

'''

n = 5

inp = [
    (172, 67),
    (183, 65),
    (180, 70),
    (170, 72),
    (181, 60)
]

re = solution(n, inp)
print('re :', re)
#=>
print('==============================')

