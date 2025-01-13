# 021 문자열 인덱싱
# letters가 바인딩하는 문자열에서 첫번째와 세번째 문자를 출력하세요.

# >> letters = 'python'
# 실행 예
# p t

letters = 'python'
print(letters[0], letters[2])

# 022 문자열 슬라이싱
# 자동차 번호가 다음과 같을 때 뒤에 4자리만 출력하세요.

# >> license_plate = "24가 2210"
# 실행 예: 2210

license_plate = "41우 7141"
print(license_plate[4:])  # me
print(license_plate[-4:])  # 정답확인

# 023 문자열 인덱싱
# 아래의 문자열에서 '홀' 만 출력하세요.

# >> string = "홀짝홀짝홀짝"
# 실행 예:
# 홀홀홀

string = "홀짝홀짝홀짝"
s = string.replace("짝", "")
print(s) # me
print(string[::2]) # 정답확인 
#=> 슬라이싱할 때 시작인덱스:끝인덱스:오프셋을 지정할 수 있습니다.

# 024 문자열 슬라이싱
# 문자열을 거꾸로 뒤집어 출력하세요.

# >> string = "PYTHON"
# 실행 예:
# NOHTYP

string = "PYTHON"
a = list(string)
a.reverse()
string = str(a)
print(string)  # me => ['N', 'O', 'H', 'T', 'Y', 'P']
print(string[::-1]) # 정답확인 

# 025 문자열 치환
# 아래의 전화번호에서 하이푼 ('-')을 제거하고 출력하세요.

# >> phone_number = "010-1111-2222"
# 실행 예
# 010 1111 2222

phone_number = "010-1111-2222"
print(phone_number.replace("-", " "))

# 026 문자열 다루기
# 25번 문제의 전화번호를 아래와 같이 모두 붙여 출력하세요.

# 실행 예
# 01011112222

print(phone_number.replace("-", ""))


# 027 문자열 다루기
# url 에 저장된 웹 페이지 주소에서 도메인을 출력하세요.

# >> url = "http://sharebook.kr"
# 실행 예:
# kr

url = "http://sharebook.kr"
print(url.index("."))
idx = url.index(".")
print(url[idx+1:])  # me 

url_split = url.split('.')  # 정답확인 
print(url_split[-1])

# 028 문자열은 immutable
# 아래 코드의 실행 결과를 예상해보세요.

# >> lang = 'python'
# >> lang[0] = 'P'
# >> print(lang)

#=> Python  예상 
lang = 'python'
#lang[0] = 'P' 
# ->  TypeError: 'str' object does not support item assignment


# 029 replace 메서드
# 아래 문자열에서 소문자 'a'를 대문자 'A'로 변경하세요.

# >> string = 'abcdfe2a354a32a'
# 실행 예:
# Abcdfe2A354A32A

string = 'abcdfe2a354a32a'
print(string.replace("a", "A"))

# 030 replace 메서드
# 아래 코드의 실행 결과를 예상해보세요.

# >> string = 'abcd'
# >> string.replace('b', 'B')
# >> print(string)

#=> aBcd 예상

# 정답확인
# abcd가 그대로 출력됩니다. 왜냐하면 문자열은 변경할 수 없는 자료형이기 때문입니다. 
# replace 메서드를 사용하면 원본은 그대로 둔채로 변경된 새로운 문자열 객체를 리턴해줍니다.
