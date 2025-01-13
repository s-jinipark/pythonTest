
# 5 + 5 * 10
# 순차적으로 계산하도록

operator = ["+", "-", "*", "/", "="]
#user_input = "5 + 5 * 10"
#user_input = input("계산식을 입력하세요 > ")

def string_calculator(user_input, show_history=False) :
    string_list = []
    lop = 0  # 마지막 연산자의 위치

    if user_input[-1] not in operator:
        user_input += "="

    for i, s in enumerate(user_input) :
        #print(i, s)
        if s in operator :  # operator 면 (연산자 나올 때까지.)
            if user_input[lop:i].strip() != "" :  # 공백 제거 후 비교
                string_list.append(user_input[lop:i])
                string_list.append(s)  # operator 도 넣어 줌
                lop = i + 1
    #print(string_list)
    string_list = string_list[:-1]
    # => '=' 연산자는 빼자

    pos = 0
    while True:
        if pos + 1 > len(string_list) :  # len() 이 1 인 경우 => 탈출 (이렇게 해도 됨)
            break
        if len(string_list) > pos + 1 and string_list[pos] in operator :
            temp = string_list[pos-1] + string_list[pos] + string_list[pos+1]
            # => 연산자 나오면 '전/연산자/후" => 계산
            del string_list[0:3]
            string_list.insert(0, str(eval(temp)))  # 맨앞에 insert
            pos = 0
        pos += 1
        if show_history :
            print(string_list)

    if len(string_list) > 0 :
        result = float(string_list[0])

    return round(result, 4)

while True :
    user_input = input("계산식을 입력하세요 (그만:exit) > ")
    if user_input == "exit" :
        break
    result = string_calculator(user_input)
    #result = string_calculator(user_input, show_history=True)
    print("결과 : {} ".format(result))