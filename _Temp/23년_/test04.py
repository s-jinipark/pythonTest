
class Shape:
    def calArea(self):
        pass

class Square( Shape):
    def __init__(self, sideLength):
        self.sideLength = sideLength

    def calArea(self):
        return self.sideLength * self.sideLength


class Rectangle(Shape):
    def __init__(self, widthLength, heightLength):
        self.widthLength = widthLength
        self.heightLength = heightLength

    def calArea(self):
        return self.widthLength * self.heightLength


class Circle(Shape ):
    def __init__(self, radiusLength):
        self.radiusLength = radiusLength

    def calArea(self):
        return int(self.radiusLength * radiusLength * 3)


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

    # for i in range(len(drawing)):
    #     answer += int(shape[i])

    # 파이썬도 Object -> int 변환이 잇음??

    return answer

drawing = [[2,5],[0,3],[1,4,6]]

solution(drawing)