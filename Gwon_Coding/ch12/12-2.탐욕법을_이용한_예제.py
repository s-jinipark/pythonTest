

'''
양수와 +, -, 그리고 괄호를 가지고 식을 만듬
그리고 괄호를 모두 지웠다
괄호를 적절히 쳐서 이 값을 최소로

(입력)
입력으로 주어지는 식의 길이는 50보다 작거나 같다

[문제 봤을 때 ..]
? 괄호를 적절히 ? -> 애매함

[책 잠깐 읽어 보면]
 1) 완전 탐색을 했을 때 시간초과가 나지 않는지 시간 복잡도 계산
 2) 문제 규칙을 찾는다
 3) 탐욕법을 생각한다

'''

#inp = '55-50+40'
inp = '10+20+30+40'

equtation = inp.split('-')
print(equtation)
answer=0

for i in equtation[0].split('+') :  # 앞에 다 더함
    answer += int(i)

for i in equtation[1:] :
    for j in i.split('+') :  # ?[ 이상하네? 마이너스(-) 나올 일 없나 ]
        answer -=int(j)

print(answer)

