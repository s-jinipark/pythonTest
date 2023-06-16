class Diet:
    def cal_calories(self):
        pass

class Food(Diet):

    def __init__(self, food_gram, calories_per_gram):
        self._food_gram = food_gram
        self._calories_per_gram = calories_per_gram

    #def calCalories (self): # 엥 , 뭐하다 이게 나왔음???
    def cal_calories(self):
        return self._food_gram * self._calories_per_gram


class Exercise(Diet):

    def __init__(self, exercise_hour, calories_per_hour):
        self._exercise_hour = exercise_hour
        self._calories_per_hour = calories_per_hour

    def cal_calories (self):
        return self._exercise_hour * self._calories_per_hour


def solution(food, exercise):
    answer = 0

    i = 0
    while i < len(food):
        f = Food(food[i][0], food[i][1])

        answer += f.cal_calories()

        i += 1

    i = 0
    while i < len(exercise):
        e = Exercise(exercise[i][0], exercise[i][1])

        answer -= e.cal_calories()
        i += 1

    return answer



food= [[100, 8], [500, 10], [200, 4]]  #  [음식량, 그램 당 칼로리]
exercise = [[1, 600], [3, 800]]  #  [운동 시간, 시간 당 소모 칼로리]
result = 3600
ans = solution(food, exercise)
print(ans)