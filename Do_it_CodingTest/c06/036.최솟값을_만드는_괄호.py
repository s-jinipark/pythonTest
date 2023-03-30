
s = '100-40+50+74-30+29-45+43+11'

'''
마이너스 기준으로 split 하고
중간에 + 할거 한 뒤 
일괄 빼준다
'''

A = list(map(str, s.split('-')))
print(A)
S = []
for aa in A:
    #print(aa)
    #print(aa.find('+'))
    if aa.find('+') > 0 :
        #print(aa)
        tmp = list(map(int, aa.split('+')))
        print(tmp)
        t_sum = 0
        for t in tmp:
            t_sum += t
        S.append(t_sum)
    else:
        S.append(int(aa))
print(S)
rst = S[0]
for j in range(1, len(S)):
    rst -= S[j]
print(rst)

##### 책 의 풀이
print('--------------------')

answer = 0
A2 = list(map(str, s.split('-')))
#-> 이 부분은 동일

def mySum(i) :  # - 로 나뉜 그룹들의 합을 구하는 함수
    sum = 0
    temp = str(i).split('+')
    for i in temp:
        sum += int(i)
    return sum

for i in range(len(A)):
    temp = mySum(A[i])
    if i == 0 :
        answer += temp
    else :
        answer -= temp

print(answer)
