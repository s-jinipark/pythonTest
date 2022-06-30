#다음과 같이 import를 사용할 수 있습니다.
#import math

def solution(s1, s2, p, q):
    #여기에 코드를 작성해주세요.
    answer = ''
    tmp_sum = 0
    # 3진수 -> 10진수
    #print(int(s1, p))
    #print(int(s2, p))  # 변환함수가 있어서 간단히...
    tmp_sum = int(s1, p) + int(s2, p)
    print(tmp_sum)
    # 바꾸고 싶은 수를 n으로 나누고 나머지와 몫을 확인한다.
    # 몫이 0이 되면 나머지들을 역순으로 문자열에 추가한다.
    while tmp_sum:
        answer = str(tmp_sum % q) + answer
        tmp_sum //= q
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
s1 = "112001"
s2 = "12010"
p = 3
q = 8
ret = solution(s1, s2, p, q)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")

#----- note -----
# 진수 변환 은 10진수를 거쳐야 하지 않나.?
# 여기처럼 3 -> 8 진수 가기 위해서는 3 -> 10 -> 8
'''
(기억이 안나 우선 인터넷 참조 했음)
n 진수 -> 10진수
int(h, 16)
int(o, 8)
int(b, 2)
'''