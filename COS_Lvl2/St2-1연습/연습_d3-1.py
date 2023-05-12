s1 = "Hello LGCNS"

# ***** 이부분 중요
s3= s1[2:7]   ## 0 부터 시작하고 마지막은 -1
print(s3)
print("s3 = ", s3)
# 결국 index 2 부터 6까지 줄력한다는

print('====================')
s1 = "Hello LGCNS "
s2 = "global reader lgcns"

print("s1 = ", s1)
print("s1.upper() = ", s1.upper())
print("s1 = ", s1)
# ***** 이부분 중요
print("s1.lower() = ", s1.lower())

print('====================')
# 문자 count, 문자 찾기
print("s1 = ", s1)
print("s1.count('l') = ", s1.count('l'))

print("s1.find('L') = ", s1.find('L'))   ## 인덱스 리턴

print('====================')
# 공백제거, 문자제거, replace
s1 = " Hello LGCNS "
s2 = "@@010-8790-1234@@"

print("s1 = ", s1)
print("s1.strip() = ", s1.strip())

print("s2 = ", s2)
print("s2.strip('@') = ", s2.strip('@'))

print("\ns1 = ", s1)
print("s1.replace() = ", s1.replace('l', 'L'))

print('====================')
# 나누기, 합치기
s1 = " Hello LGCNS "
s2 = "010 8790 1234"
s3 = "010--8769"
s4 = "010-5793-8769"

print("s1 = ", s1)
splitList1 = s1.split()
print("s1.split() = ", splitList1)

print("\ns3 = ", s4)
splitList4 = s4.split('-')
print("s4.split('-') = ", splitList4)

# ***** 이부분 중요
print("\nJoin Test")
strJoin = '*'.join(splitList4)
print(strJoin)

print("문자열 길이")
size = len(s4)
print(size)

print("문자열을 리스트로")
sample = list(s1)
print(sample)

