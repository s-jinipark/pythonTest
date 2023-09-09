
def solution(marks):
    answer = ''
    tot = len(marks)
    ok = 0
    for m in marks :
        print(m)
        if m == "O" :
            ok += 1
    answer = str(ok) + "/" + str(tot)
    return answer



marks = ["O", "O", "X", "X", "O"]

an = solution(marks)
print(an)