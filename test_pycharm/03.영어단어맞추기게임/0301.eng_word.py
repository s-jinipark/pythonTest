import random

words_dict = {
    "사자":"lion",
    "호랑이":"tiger",
    "사과":"apple",
    "비행기":"airplane"
}
# 한글이 key, 영어가 값

# dict 는 순서의 개념이 없으므로 list 에 담는다
words = []

for word in words_dict :
    words.append(word)
    print(word +  " / " + words_dict[word])

random.shuffle(words)

chance = 3
for i in range(0, len(words)) :
    q = words[i]
    for j in range(0, chance) :  # 3회 시도
        user_input = str(input("{} 의 영어 단어를 입력하세요>".format(q)))
        english = words_dict[q]  # 값을 참조

        if english.lower() == user_input.strip().lower() :  # 공백 없애고 소문자로 비교
            print("정답입니다.")
            break
        else :
            print("틀렸습니다.")
    if user_input != english :
        print("정답은 {} 입니다.".format(english))

print("모든 문제 제출 !! ")