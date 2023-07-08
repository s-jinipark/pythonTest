
##### Anagram(아나그램 : 구글 인터뷰 문제)

def solution():
    #answer = 0
    answer = ''
    '''
    이것도 dict 이용하면 될 듯
    '''
    # 두 단어만 넘어 온다는 거잖아
    temp = dict()

    # dict 에 구성을 다 넣은 뒤
    # -1 해주고 나중에 0 이 아닌거 있으면 NO
    for i in inp1:
        if i not in temp:
            temp[i] =1
        else :
            temp[i] += 1
    print(temp)

    for j in inp2:
        if j in temp:
            temp[j] -= 1

    print(temp)

    # chk
    answer = 'YES'
    for k in temp:
        if temp[k] != 0:
            answer = 'NO'
            break

    return answer


inp1 = 'AbaAeCe'
inp2 = 'baeeACA'

re = solution()
print(re)
#=>
print('====================')

inp1 = 'ABCEFGHIJKLMNPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
inp2 = 'bcdEfgHiJKLmnopRSstVvXYZzABCeFGhIjklMNPQqrTUuWwxya'

re = solution()
print(re)