
##### 회문 문자열 검사
def solution():
    answer = 0

    for i in inp:
        tmp = i.lower()
        #print(연습)
        rtn = 'YES'
        for j in range(len(tmp)//2):
            #print(j)
            comp = len(tmp)-1-j
            #print(연습[j], 연습[comp])
            if tmp[j] != tmp[comp]:
                rtn='NO'
                break
        print(i, rtn)
    return answer

N = 5
inp = ['level', 'moon', 'abcba', 'soon', 'gooG']
re = solution()
print(re)
#=>


N = 10
inp = ['skgjkjdkjgkksjgk', 'sssssssssssssssksssssssssssssss',
'osdddddddddddddddddddddddso', 'sksdddddddddddddddddddddddddddddddddddddddkss',
'skskskuuuuuuuuuuuuuuuuuuUuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuksksks', 'stts', 'moon', 'abcba', 'yes', 'eyE']
re = solution()
print(re)
#=>
'''
#1 NO
#2 YES
#3 YES
#4 NO
#5 YES
#6 YES
#7 NO
#8 YES
#9 NO
#10 YES
'''