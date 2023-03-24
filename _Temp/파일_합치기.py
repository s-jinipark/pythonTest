
# 그냥 읽음
# f = open('test1.txt', 'r')
# while True:
#     line = f.readline()
#
#     if not line: break
#     print(line)
# f.close()

# 하나의 문장으로 만들어야 해서..
# f = open('test1.txt', 'r')
# lines = f.readlines()
# for line in lines:
#     line = line.strip()  # 줄 끝의 줄 바꿈 문자를 제거한다.
#     if '.' in line :
#         print(line)
#     else:
#         print(line, end='')
# f.close()


'''
[오류 발생]
ERROR: Could not install packages due to an OSError: HTTPSConnectionPool(host='files.pythonhosted.org', port=443): Max retries exceeded with url: /packages/71/3a/3b1
9effdd4c03958b90f40fe01c93de6d5280e03843cc5adf6956bfc9512/googletrans-3.0.0.tar.gz (Caused by SSLError(SSLCertVerificationError(1, '[SSL: CERTIFICATE_VERIFY_FAILED] 

[해결책]
$ pip install --trusted-host pypi.python.org --trusted-host files.pythonhosted.org --trusted-host pypi.org 설치할패키지이름
or
$ python3 -m pip install --trusted-host pypi.python.org --trusted-host files.pythonhosted.org --trusted-host pypi.org 설치할패키지이름
'''

# 위를 종합해서
##### 1 단계
import googletrans
# import requests
# response = requests.get("https://translate.google.com/", verify=False)

translator = googletrans.Translator()

n = "259"
#org_file = "test" + n + ".txt"
#org_file = "9-28.txt"
#org_file = r"D:\임시\쿠베 파일\30-48 .txt"
org_file = r"D:\임시\쿠베 파일\259-273.txt"
first_file = "영어파일" + n + ".txt"
second_file = "한글파일" + n + ".txt"

f = open(org_file, 'r')
f2 = open(first_file, 'w')
lines = f.readlines()
for line in lines:
    line = line.strip()  # 줄 끝의 줄 바꿈 문자를 제거한다.
    # if '.' in line :
    #     print(line)
    # else:
    #     print(line, end='')
    if '.' in line :
        f2.write(line)
        f2.write('\n')
    else:
        f2.write(line)
f.close()
f2.close()

##### 2 단계


# with open(first_file, 'r') as f :
#     readLines = f.readlines()
#
# for lines in readLines:
#     print(lines)
#     result1 = translator.translate(lines, dest='ko')
#     print(result1.text)
#     with open(second_file,'a', encoding='UTF8') as f:
#         f.write(result1.text + '\n')

'''
httpcore._exceptions.ConnectError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: 
self signed certificate in certificate chain (_ssl.c:997)

'''

