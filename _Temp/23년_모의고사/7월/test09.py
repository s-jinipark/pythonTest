
def solution(emails):
    answer = 0

    # 정규식을 적용하면 쉬울 것 같은데.. 흠
    # 일단 @ 와 . 이 있어야 함 + 한개 씩 만
    # 순서 -> @ 나온 뒤 .
    # 사이에는 알파벳 소문자 적어도 한 개 이상

    for e in emails:

        if e.find("@") == -1 or e.find(".") == -1:
            continue
        if e.find("@") +1 ==  e.find("."):
            continue
        print(e, e.find("@"), e.find("."))
        # 3단계로 나눠
        #print(e[:e.find("@")], e[e.find("@")+1:e.find(".")], e[e.find(".")+1:])
        part1 = e[:e.find("@")]
        part2 = e[e.find("@")+1:e.find(".")]
        part3 = e[e.find(".")+1:]
        print(part1, part2, part3)
        if part1.isalpha() and part2.isalpha() and part3.isalpha():
            answer +=1

    return answer


emails = ["example@example.com", "example@example", "example@.com"]

an = solution(emails)

print(an)