
# Diet 클래스_빈칸채우기

class Diet:
    def cal_calories(self):
        pass

class Food(Diet):

    def __init__(self, food_gram, calories_per_gram):
        self._food_gram = food_gram
        self._calories_per_gram = calories_per_gram

    #def calCalories(self):
    # 이거 함정.. 보기에는 calCalories 로 나옴
    def cal_calories(self):
        return self._food_gram * self._calories_per_gram


class Exercise(Diet):

    def __init__(self, exercise_hour, calories_per_hour):
        self._exercise_hour = exercise_hour
        self._calories_per_hour = calories_per_hour

    #def calCalories(self):
    def cal_calories(self):
        return self._exercise_hour * self._calories_per_hour


def solution(food, exercise):
    answer = 0

    i = 0
    while i < len(food):
        f = Food(food[i][0],food[i][1])
        answer += f.cal_calories()
        i += 1

    i = 0
    while i < len(exercise):
        e = Exercise(exercise[i][0],exercise[i][1])
        answer -= e.cal_calories()
        i += 1

    return answer


food = [[100, 8], [500, 10], [200, 4]]
exercise = [[1, 600], [3, 800]]

an = solution(food, exercise)
print(an)


'''
    answer += int(f.cal_calories())
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'NoneType'

=>

    #def calCalories(self):
    # 이거 함정.. 보기에는 calCalories 로 나옴
    def cal_calories(self):

'''