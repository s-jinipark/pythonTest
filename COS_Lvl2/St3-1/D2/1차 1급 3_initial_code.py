def func_a(numA, numB, exp):
    if exp == '+':
        return numA + numB
    elif exp == '-':
        return numA - numB
    elif exp == '*':
        return numA * numB
    
def func_b(exp):
    for index, value in enumerate(exp):
        if value == '+' or value == '-' or value == '*':
            return index
        
def func_c(exp, idx):
    numA = int(exp[:idx])
    numB = int(exp[idx + 1:])
    return numA, numB

def solution(expression):
    # exp_index = func_@@@(@@@)
    # first_num, second_num = func_@@@(@@@)
    # result = func_@@@(@@@)
    exp_index = func_b(expression)
    first_num, second_num = func_c(expression, exp_index)
    result = func_a(first_num, second_num, expression[exp_index])
    return result

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
expression = "123+12"
ret = solution(expression)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("Solution: return value of the function is", ret, ".")