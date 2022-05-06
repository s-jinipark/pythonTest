def solution(characters):
    result = ""
    result += characters[0]
    #for i in range(len(characters)):
    for i in range(1, len(characters)):
        #print(characters[i])
        if characters[i - 1] != characters[i]:
            result += characters[i]
        #print(result)
    return result

#The following is code to output testcase. The code below is correct and you shall correct solution function.
characters = "senteeeencccccceeee"
ret = solution(characters)

#Press Run button to receive output.
print("Solution: return value of the function is", ret, ".")