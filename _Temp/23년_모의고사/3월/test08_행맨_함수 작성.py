
def solution(word, question):
    answer = []

    # set 에 담아 놓고 지우는 걸로.
    # s = set()
    # for w in word:
    #     s.add(w)
    # ** 여기는 이렇게
    s = set(word)
    print(s)

    for q in question :
        if q in s :
            answer.append("YES")
            s.remove(q)
        else :
            answer.append("NO")
        if len(s) == 0 :
            answer.append("SUCCESS")
            break

    if len(s) > 0:
        answer.append("FAIL")

    return answer


word = "happy"   # pp 는 한번만 나오면 YES
question = ["a", "e", "i", "o", "u", "p", "h", "x", "y", "j", "r"]

an = solution(word, question)
print(an)