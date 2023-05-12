def solution(s, skip, index):
    answer = ''
    skip_list = []
    for sc in skip :
        skip_list.append(ord(sc))
    print(skip_list)

    for c in s:
        print(ord(c))   # a : 97 , z : 122
        tmp = ord(c)
        tmp_idx = index
        while tmp_idx > 0 :
            tmp += 1
            # 숫자가 넘어가면 원복
            if tmp > 122:
                tmp = tmp % 122 + 97 - 1

            if tmp in skip_list:
                print('>>', tmp)
            else :
                tmp_idx -= 1
                print('>', tmp)
        answer += chr(tmp)

    # test = 123
    # print(test%122+97-1)
    # print(chr(test%122+97-1))

    return answer



s ="aukks"
skip ="wbqd"
index = 5
re = solution(s, skip, index)

print(re)

print("====================")

