#You may use import as below.
#import math

def solution(shirt_size):
    #Write code here.
    #answer = []
    answer = [0, 0, 0, 0, 0, 0]  # [ "XS" 개수 , "S" 개수 , "M" 개수 , "L" 개수 , "XL" 개수 , "XXL" 개수 ]
    for ss in shirt_size :
        #print(ss)
        if ss == 'XS' :
            answer[0] = answer[0] +1
        elif ss == 'S' :
            answer[1] = answer[1] + 1
        elif ss == 'M' :
            answer[2] = answer[2] + 1
        elif ss == 'L' :
            answer[3] = answer[3] + 1
        elif ss == 'XL' :
            answer[4] = answer[4] + 1
        elif ss == 'XXL' :
            answer[5] = answer[5] + 1

    return answer

#The following is code to output testcase.
shirt_size = ["XS", "S", "L", "L", "XL", "S"]
ret = solution(shirt_size);

#Press Run button to receive output.
print("Solution: return value of the function is ", ret, " .")