def solution(n, words):
    answer = []
    last_w = words[0][0]
    #print(last_w)
    cnt = 0
    rec_list = []
    for w in words:
        #print(w)
        if last_w != w[0] :
            break
        if len(w) == 1 :
            break
        if w in rec_list :
            break
        cnt += 1
        last_w = w[-1]
        rec_list.append(w)
    #print(len(words) , cnt)
    if len(words) == cnt :
        answer.append(0)
        answer.append(0)
    else :
        # 몇번째 사람이 몇번째 차례
        #print(cnt % n)
        #print(cnt // n)
        tun = (cnt % n) + 1
        ord = (cnt // n) + 1  # 차례
        answer.append(tun)
        answer.append(ord)
    return answer


n = 3
words = ['tank', 'kick', 'know', 'wheel', 'land', 'dream', 'mother', 'robot', 'tank']
res = solution(n, words)
print(res)     # [3, 3]

n = 5
words = ['hello', 'observe', 'effect', 'take', 'either', 'recognize', 'encourage', 'ensure', 'establish', 'hang', 'gather', 'refer', 'reference', 'estimate', 'executive']
res = solution(n, words)
print(res)     # [0, 0]

n = 2
words = ['hello', 'one', 'even', 'never', 'now', 'world', 'draw']
res = solution(n, words)
print(res)    # [1, 3]

