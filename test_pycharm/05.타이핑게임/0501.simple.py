import time
import random

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

    correct = 0
    for i, c in enumerate(user_input) :
        if i >= len(q):   # q 의 글자 수 까지만 계산하겠다는
            break
        if c == q[i] :   # 동일하면 correct 증가
            correct += 1

    total_len = len(q)
    c = correct / total_len * 100
    e = (total_len-correct) / total_len * 100
    speed = (correct / end_time) * 60

    print("속도 : {:0.2f} , 정확도 : {:0.2f} , 오타율 : {:0.2f} ".format(speed, c, e))
