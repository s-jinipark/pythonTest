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

    # for i in range(len(friends)):
    #     @ @ @ @ @        ;
    #
    #     if @ @ @ @ @ == @ @ @ @ @:
    #         return "We are friends."
    #     else:
    #         return "We are not friends."


n = 5
friends = [[1,2], [2,3], [3,4]]
x = 1
y = 4
an = solution(n, friends, x, y)
print(an)