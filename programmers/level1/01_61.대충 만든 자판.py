def short_press(c, keymap) :
    minVal = 999
    for k in keymap:
        for i in range(len(k)) :
            print('>', k[i])
            print('>>', k[i].find(c))
            if c == k[i] and minVal > i:
                minVal = i
                break
    if minVal == 999:
        minVal = -1
    else :
        minVal += 1
    return minVal

def solution(keymap, targets):
    answer = []

    for t in targets :
        #print(t)
        sum = 0
        for c in t :
            print(c)
            print(short_press(c, keymap))
            tmp = short_press(c, keymap)
            sum += tmp
        answer.append(sum)

    return answer


keymap = ["ABACD", "BCEFD"]
targets = ["ABCD","AABB"]

re = solution(keymap, targets)

print(re)

print("====================")

