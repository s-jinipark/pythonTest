
# 반복문 while

guest = 1
while guest < 10:
    print("손님이 {}명 입니다.".format(guest))
    guest = guest +1
    if guest ==10:
        print("손님이 꼭 찼습니다.")


num = 1

while num <= 10:
    if num % 2 == 0:
        print("짝 {}".format(num))
    else:
        print("홀 {}".format(num))
    num += 1


num = 1
hap = 0

while num <=100:
    hap += num
    num += 1
print(hap)


# 반복문 for
print("-----")
a = "abcdefg"
for i in a:
    print(i)

print("-----")
a = ["python", "java", "c/c++", "C#"]
for i in a:
    print(i)

print("-----")
for i in range(5+1):
    print(i)

print("-----")
for i in range(1, 10, 2):
    print(i)  

print("-----")
a = [(1,2), (3,4), (5,6)]
for i in a:
    for j in i:
        print(j)  

print("-----")
student = [{"홍길동":100} , {"가제트":200} , {"가가멜":300}]
for i in student:
    data = (list(i.items())[0])
    name = data[0]
    value = data[1]
    print("이름 : {}  점수 : {}".format(name, value))

print("-----")
msg = "python programming"
for s, i in enumerate(msg, start=1):
    print(s, i)

print("-----")
result = []
for num in range(1,6):
    result.append(num + 5)
print(result)

print("-----")
result = [num + 5 for num in range(1,6)]
print(result)

print("-----")
result = [num *3 for num in range(1,99) if num % 2 == 0]
print(result)

print("-----")
for i in range(2, 10):
    for j in range(1,10):
        result = i * j
        print("{} X {} = {}".format(i,j, result))

#컴프리핸션
gugu = ["{} X {} = {}".format(i,j, i*j) for i in range(2,10) for j in range(1,10)]
print(gugu)


###
print("=====")
num = 0
while True:
    print(num)
    num += 1

    if num == 10:
        break

print("-----")
num = 0
while num < 10:
    num += 1
    if num == 5:
        continue
    print(num)

