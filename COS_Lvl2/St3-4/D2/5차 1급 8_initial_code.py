def func_a(a, b):
	mod = a % b
	while mod > 0:
		a = b
		b = mod
		mod = a % b
	return b

def func_b(n):
	answer = 0
	for i in range(1, n+1):
		if func_c(n, i):
			answer += 1
	return answer

def func_c(p, q):
	if p % q == 0:
		return True
	else:
		return False

def solution(a, b, c):
	answer = 0
	gcd = func_a(func_a(a, b), c)
	answer = func_b(gcd)
	return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
a = 24
b = 9
c = 15
ret = solution(a, b, c)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")

'''
공약수 구하는 방법
 두 수가 ? 로 나누어지는지 판별 : 동시에 나누어지면 공약수
 두 수가 한 수 까지 나누어지는지 반복한다. : 최대공약수 < 현재까지

(잘 몰라 솔루션 참조)
'''