def solution(in1, in2):
    answer = 0
    ilist = in2.split()
    x = 1
    y = 1
    for i in ilist :
        print(i)
        if i == "R" and y < int(in1) :
            y +=1
        elif i == "U" and x > 1 :
            x -=1
        elif i == "D" and x < int(in1) :
            x +=1
        elif i == "L" and y > 0 :
            y -=1
    print (x, y)

    return answer



inp1 = "5"
inp2 = "R R R U D D"

print("----- -----")
print(solution(inp1, inp2))


