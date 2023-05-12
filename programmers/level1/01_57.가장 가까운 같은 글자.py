def solution(s):
    answer = []
    dict = {}

    for i in range(len(s)):
        print(s[i])
        if s[i] in dict :
            #dict[i] = i
            tmp = i - dict[s[i]]
            answer.append(tmp)
        else :
            #dict[i] = i
            answer.append(-1)
        dict[s[i]] = i
    print(dict)

    return answer


#s = "banana"
s = "foobar"

re = solution(s)
print(re)

print("====================")

