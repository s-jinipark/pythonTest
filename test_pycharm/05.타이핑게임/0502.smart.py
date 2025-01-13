
'''
한글 = ((초성 * 21) + 중성) * 28 + 종성 + 44032
  : 44032 는 '가' 에 해당하는 유니코드 'AC00' 의 10진수 값

초성 = ((x - 44032) /28 ) / 21
중성 = ((x - 44032) /28 ) % 21
종성 = (x - 44032) % 28
'''

CHO = ["ㄱ", "ㄲ", "ㄴ", "ㄷ", "ㄸ", "ㄹ", "ㅁ", "ㅂ", "ㅃ", "ㅅ", "ㅆ", "ㅇ", "ㅈ", "ㅉ", "ㅊ", "ㅋ", "ㅌ", "ㅍ", "ㅎ"]
JUNG = ["ㅏ","ㅐ","ㅑ","ㅒ","ㅓ","ㅔ","ㅕ","ㅖ","ㅗ","ㅘ","ㅙ","ㅚ","ㅛ","ㅠ","ㅝ","ㅞ","ㅟ","ㅠ","ㅡ","ㅢ","ㅣ"]
JONG = ["","ㄱ","ㄲ","ㄳ","ㄴ","ㄵ","ㄶ","ㄷ","ㄹ","ㄺ","ㄻ","ㄼ","ㄽ","ㄾ","ㄿ","ㅀ","ㅁ","ㅂ","ㅄ","ㅅ","ㅆ","ㅇ","ㅈ","ㅊ","ㅋ","ㅌ","ㅍ","ㅎ"]

print(len(CHO))
print(len(JUNG))
print(len(JONG))

print(  chr(((0*21)+0) * 28 + 0 + 44032) )
# => '가'
print(  chr(((0*21)+0) * 28 + 1 + 44032) )
# => '각'
print(  chr(((2*21)+0) * 28 + 1 + 44032) )
# => '낙'

user_input = input("입력 > ")
word_list = list(user_input)
print(word_list)

break_word = []
for k in word_list :
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

print("입력 : {} ".format(user_input))
print("입력 : {} ".format(break_word))

