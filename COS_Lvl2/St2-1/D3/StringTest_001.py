#문자열 인덱스 사용 및 슬라이싱
s1 = "Hello LGCNS"
print("s1 = ", s1)

s2 = s1[3]
print("s2=", s2)

s3= s1[2:7]   ## 0 부터 시작하고 마지막은 -1
print(s3)
print("s3 = ", s3)

#문자열과 문자열 변수를 더할 수 있다.
s4 = "LGCNS"
s5 = "Global Reader " + s4  ## ㅎㅎ Reader ..

print("s4 = ", s4)
print("s5 = ", s5)

#문자열과 문자열을 더할 수 있다.
s6 = "Global Reader " + "LGCNS"
print("s6 = ", s6)

#숫자를 문자열과 더하기위해 변환한다. 
s7 = "LGCNS" + str(1) + "위"
print("s7 = ", s7)


