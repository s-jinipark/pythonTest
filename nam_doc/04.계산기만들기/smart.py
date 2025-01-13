
operator = ["+", "-", "*", "/", "="]
#user_input = "5 + 5 * 10"
user_input = "10 + 20 + 30 * 2"

string_list = []

# for s in user_input :
#     print(s)

lop = 0 # last op pos , 마지막 OP 위치

# [2] 마지막에 "=" 붙여 줌
if user_input[-1] not in operator:
    user_input += "="

for i, s in enumerate(user_input) :
    #print(i, s)
    if s in operator:
        if user_input[lop:i].strip() != "":
            string_list.append(user_input[lop:i]) # 연산자 앞까지 ..
            string_list.append(s)  # 연산자 추가
            lop = i +1 # 갱신
# 처음시도, 마지막 숫자가 안나옴 
# [2] string 끝에 "=" 붙여 처리 ...
# 했다가 다시 "=" 제거
string_list = string_list[:-1]
print(string_list) 

pos = 0
while True:
    if pos +1 > len(string_list):
        break
    if len(string_list) > pos +1 and string_list[pos] in operator :
        temp = string_list[pos-1] + string_list[pos] + string_list[pos+1]
        del string_list[0:3]  # 지워버린다
        string_list.insert(0, str(eval(temp))) # eval 로 계산
        pos = 0
    pos += 1
    print(string_list)



