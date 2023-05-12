def solution(babbling):
    answer = 0
    #print(babbling)
    can = ["aya", "ye", "woo", "ma" ]
    for b in babbling :
        print(b)
        leng = len(b)
        for c in can:
            #print(b.replace(c, ""))
            b = b.replace(c, "*")
            print(b)
        for i in range(len(b)):
            if b[i] != '*':
                break
        else :
            answer += 1
        print('answer: ' , answer)
    return answer

#inp = ["aya", "yee", "u", "maa", "wyeoo"]
inp = ["ayaye", "uuuma", "ye", "yemawoo", "ayaa"]
re = solution(inp)
print(re)