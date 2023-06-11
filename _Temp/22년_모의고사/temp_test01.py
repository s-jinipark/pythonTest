

def solution(alpha):
    dat = [0] *200

    for line in alpha:
        for ch in line:
            #print(ch)
            dat[ord(ch)] += 1

    result = ''
    for i in range(200):
        if dat[i] == 0 : continue
        print(chr(i), dat[i])
        for x in range(dat[i]):
            result += chr(i)

    return result

alpha = ['ABC', 'AGH', 'HIJ', 'KAB', 'ABC']
solution(alpha)

d = dict()

for a in alpha:
    for c in a:
        #print(c)
        if c not in d : d[c] = 0
        d[c] += 1

#a = 10
# 여기 break 걸고 debug 로 본다

for i in range(26):
    ch = chr(ord('A') + i)
    #print(ch)
    if ch not in d: continue

    for x in range(d[ch]):
        print(ch, end = '')
        
a = 10

