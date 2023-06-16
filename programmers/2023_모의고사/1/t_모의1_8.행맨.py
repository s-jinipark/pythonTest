
def solution(word, question):
    answer = []
    # 문제를 읽어 보면 중복된거는 하나로 치는 듯
    tmp = set(word)
    print(tmp)  # 이렇게 넣으면 분리되어 들어감
                # 단어 통째로 넣으려면 => tmp.add('apple')

    for q in question:
        if q in word :
            answer.append('Yes')
            tmp.remove(q)
            if len(tmp) == 0:
                answer.append('SUCCESS')
                break
        else:
            answer.append('No')

    if len(tmp) > 0:
        answer.append('FAIL')
    return answer


word ="happy"
question = ["a", "e", "i", "o", "u", "p", "h", "x", "y", "j", "r"]

ans = solution(word, question)
print(ans)


word ="dog"
question =["a", "b", "c", "d", "e", "f", "h", "i", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "u", "v"]

ans = solution(word, question)
print(ans)
