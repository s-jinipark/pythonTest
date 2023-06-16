def solution(names):
    answer = []
    tmp = set()
    for n in names:
        tmp.add(n)
    print(tmp)
    answer = list(tmp)
    answer.sort()
    return answer

names = ["Amy", "Carol", "Bob", "Amy"]

ans= solution(names)
print('ans:', ans)
