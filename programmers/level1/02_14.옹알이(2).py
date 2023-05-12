
# 아직

def solution(babbling):
    answer = 0
    canlist = ["aya", "ye", "woo", "ma" ]

    for b in babbling:
        print(b)
        for c in canlist:
            if c+c in b:
                # 이 경우 꽝
                break
        while True :
            for c in canlist:
                if c in b:
                    print(c, b)
                    b = b.replace(c, '')


    return answer

babbling = ["aya", "yee", "u", "maa"]

re = solution(babbling)
print(re)

