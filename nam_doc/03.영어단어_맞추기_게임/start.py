
# 영어 단어 맞추기 게임 (파이썬기초, 랜덤함수, 반복문, 조건문, 딕셔너리)

import random

words_dict = {
    "사자":"lion",
    "호랑이":"tiger",
    "사과": "apple",
    "비행기": "airplane"
}
# -> 순서이 개념없어서 list 에 담아 순차적으로..

words = []

for word in words_dict:
    words.append(word)  # key만 리스트에

#print(words)

random.shuffle(words) # 섞어 줌

chance = 3

for i in range(0, len(words)):
    q = words[i]  # 한 문제 꺼내 옴
    for j in range(0, chance):
        user_input = str(input("{} 의 영어단어를 입력하세요> ".format(q)))
        english = words_dict[q]  # 영단어 셋팅
    
        if user_input.strip().lower() == english.lower() :
            print("정답입니다.")
            break
        else:
            print("틀렸습니다.")
    if user_input.strip().lower() == english.lower() :
        print("정답은 {} 입니다.".format(english))

print("모든 문제를 다 제출했습니다.")

