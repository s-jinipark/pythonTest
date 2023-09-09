parent = [0 for _ in range(10001)]


def func_a(num):
    if num == parent[num]:
        return num
    else:
        parent[num] = func_a(parent[num])
        return parent[num]


def func_b(x, y):
    x = func_a(x)
    y = func_a(y)
    parent[y] = x


def solution(n, friends, x, y):
    for i in range(0, n + 1):
        parent[i] = i
    print(parent)

    for i in range(len(friends)):
        print(friends[i][0], friends[i][1])
        func_b(friends[i][0], friends[i][1])
        #@ @ @ @ @        ;
    print(parent)

    # if @ @ @ @ @ == @ @ @ @ @:
    #if parent[x] == parent[y]:  # 부분 정답
    if func_a(x) == func_a(y):
        return "We are friends."
    else:
        return "We are not friends."


n = 5   # 총 n명의 사람들이 이용하는 메신저
friends = [[1,2], [2,3], [3,4]]
x = 1
y = 4
'''
x 와 y 가 친구 관계인가?
1번 사람과 2번 사람이 친구 관계이고 2번 사람과 3번 사람이 친구 관계이면, 
자동으로 1번 사람과 3번 사람도 친구 관계가 됩

'''
an = solution(n, friends, x, y)
print(an)