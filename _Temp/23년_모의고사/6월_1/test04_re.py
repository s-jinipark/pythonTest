
class Shape:
    def calArea(self):
        pass

class Square( Shape):   # <- 빈칸
    def __init__(self, sideLength):
        self.sideLength = sideLength

    def calArea(self):
        return self.sideLength * self.sideLength   # <- 빈칸


class Rectangle(Shape):   # <- 빈칸
    def __init__(self, widthLength, heightLength):
        self.widthLength = widthLength
        self.heightLength = heightLength

    def calArea(self):
        return self.widthLength * self.heightLength   # <- 빈칸


class Circle(Shape ):   # <- 빈칸
    def __init__(self, radiusLength):
        self.radiusLength = radiusLength

    def calArea(self):
        return self.radiusLength * self.radiusLength * 3  # <- 빈칸


def solution(drawing):
    shape = [None] * 100

    for i in range(len(drawing)):
        if drawing[i][0] == 0:
            shape[i] = Square(drawing[i][1])
        elif drawing[i][0] == 1:
            shape[i] = Rectangle(drawing[i][1], drawing[i][2])
        elif drawing[i][0] == 2:
            shape[i] = Circle(drawing[i][1])

    answer = 0

    print(shape)

    for i in range(len(drawing)):
        answer += shape[i].calArea()   # <- 빈칸

    # [오류] TypeError: unsupported operand type(s) for +=: 'int' and 'Circle'
    # calArea() 호출하는 것을 까먹음

    return answer

drawing = [[2,5],[0,3],[1,4,6]]

ans = solution(drawing)
print('ans: ' , ans)