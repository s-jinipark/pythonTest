
#파이썬에서 파일 읽고 쓰기


file = open("sample.txt", mode="w", encoding="utf-8")
file.write("hello python")
file.write("안녕 파이썬")
file.close()  #(중요)[파일 사용후 close() 하지 않으면]
                # 다른 프로그램 및 객체에서 접근하지 못하는
                # 현상이 생길 수 있습니다.

rfile = open("sample.txt", mode="r", encoding="utf-8")
content = rfile.read()
rfile.close

print(content)


with open("sample.txt", mode="r", encoding="utf-8") as file:
    print(file.read())
# [with 를 같이 사용하면 close 안 해도 됨] 

