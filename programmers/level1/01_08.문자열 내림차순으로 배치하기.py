def solution(s):
    answer = ''
    lst = list(s)
    lst.sort(reverse=True)
    print(lst)
    for l in lst :
        answer += l
    return answer

s = "Zbcdefg"

re = solution(s)
print(re)

print("====================")
