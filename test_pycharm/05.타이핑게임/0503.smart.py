import os
import time
import random

'''
한글 = ((초성 * 21) + 중성) * 28 + 종성 + 44032
  : 44032 는 '가' 에 해당하는 유니코드 'AC00' 의 10진수 값
  : AC00 부터 시작
초성 = ((x - 44032) /28 ) / 21
중성 = ((x - 44032) /28 ) % 21
종성 = (x - 44032) % 28
'''

CHO = ["ㄱ", "ㄲ", "ㄴ", "ㄷ", "ㄸ", "ㄹ", "ㅁ", "ㅂ", "ㅃ", "ㅅ", "ㅆ", "ㅇ", "ㅈ", "ㅉ", "ㅊ", "ㅋ", "ㅌ", "ㅍ", "ㅎ"]
JUNG = ["ㅏ","ㅐ","ㅑ","ㅒ","ㅓ","ㅔ","ㅕ","ㅖ","ㅗ","ㅘ","ㅙ","ㅚ","ㅛ","ㅠ","ㅝ","ㅞ","ㅟ","ㅠ","ㅡ","ㅢ","ㅣ"]
JONG = ["","ㄱ","ㄲ","ㄳ","ㄴ","ㄵ","ㄶ","ㄷ","ㄹ","ㄺ","ㄻ","ㄼ","ㄽ","ㄾ","ㄿ","ㅀ","ㅁ","ㅂ","ㅄ","ㅅ","ㅆ","ㅇ","ㅈ","ㅊ","ㅋ","ㅌ","ㅍ","ㅎ"]
'''
print(len(CHO))
print(len(JUNG))
print(len(JONG))

print(  chr(((0*21)+0) * 28 + 0 + 44032) )
# => '가'
print(  chr(((0*21)+0) * 28 + 1 + 44032) )
# => '각'
print(  chr(((2*21)+0) * 28 + 1 + 44032) )
# => '낙'
'''

def break_korean(string) :
    #user_input = input("입력 > ")
    #word_list = list(user_input)
    #print(word_list)

    break_word = []
    #for k in word_list :
    for k in string:
        if ord(k) >= ord("가") and ord(k) <= ord("힣") :
            # 유니코드 상 몇번째 글자인지 인덱스를 구함
            char_index = ord(k) - ord('가')

            # 초성 = (유니코드인덱스 / 28) / 21
            char1 = int((char_index / 28) / 21)
            break_word.append(CHO[char1])

            # 중성 = (유니코드인덱스 / 28) % 21
            char2 = int((char_index / 28) % 21)
            break_word.append(JUNG[char2])

            # 종성 = 유니코드인덱스 % 28
            char3 = int(char_index % 28)

            if char3 > 0 :
                break_word.append(JONG[char3])
        else :
            break_word.append(k)
    return break_word


WORD_LIST = [
    "대한민국 베스트셀러 여행지",
    "마이클 샌델 정의란 무엇인가",
    "명리: 운명을 읽다",
    "베스트셀러 책쓰기 기술 : 재미있고 읽기쉬운 사례 중심의",
    "베스트셀러의 저자들 : 한국인의 정신을 정초한 천년 베스트셀러의 저자들",
    "베스트셀러 세트: 반찬이 필요 없는 밥 요리+백종원이 추천하는 집밥 메뉴 52",
    "혜민 스님 베스트셀러 세트",
    "베스트셀러 작가들의 글쓰기 비법 : 그들의 글쓰기는 뭐가 다를까?"
]

# 리스트를 섞음
random.shuffle(WORD_LIST)

for q in WORD_LIST :
    start_time = time.time()   # 시작 시간
    user_input = str(input(q + '\n')).strip()   # q 를 주고 다음줄에...
    end_time = time.time() - start_time   # 계산

    # [2] 추가
    src = break_korean(q)
    tar = break_korean(user_input)

    if user_input == "/exit" :
        break

    correct = 0
    #for i, c in enumerate(user_input) :
    for i, c in enumerate(tar):
        #if i >= len(q):   # q 의 글자 수 까지만 계산하겠다는
        if i >= len(src):
            break
        #if c == q[i] :   # 동일하면 correct 증가
        if c == src[i]:
            correct += 1

    #total_len = len(q)
    total_len = len(src)
    c = correct / total_len * 100
    e = (total_len-correct) / total_len * 100
    speed = (correct / end_time) * 60

    print("속도 : {:0.2f} , 정확도 : {:0.2f} , 오타율 : {:0.2f} ".format(speed, c, e))
    os.system("pause")

'''
참조
https://30aichallenge.tistory.com/108?category=941850
'''
