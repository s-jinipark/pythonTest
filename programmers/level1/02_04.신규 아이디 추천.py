
def solution(new_id):
    answer = ''
    # 1단계
    print(new_id.lower())
    answer = new_id.lower()

    # 2단계
    tmp = ''
    for a in answer:
        #print(a)
        if a.isalnum() or a in ['-', '_', '.'] :
            tmp += a
    answer = tmp
    print(answer)

    # 3단계
    while answer.find('..') >-1:
        answer = answer.replace('..', '.')
    print(answer)

    # 4단계
    front = answer.find('.')
    back = answer.rfind('.')
    print(front, back)
    # 뒤 부터
    if back == len(answer)-1:
        answer = answer[:len(answer)-1]
    if front == 0:
        answer = answer[1:]
    print('>', answer)

    # 5단계
    # while answer.find(' ') >-1:
    #     answer = answer.replace(' ', 'a')
    # '' 이 경우 -> 'a' 로 변경해야 되서
    print(len(answer))
    if len(answer) == 0:
        answer = 'a'
    for i in range(len(answer)):
        if answer[i] == '' :
            answer[i] = 'a'
    print(answer)

    # 6단계
    #print('>', len(answer))
    if len(answer) >= 16:
        answer = answer[:15]
    back = answer.rfind('.')
    if back == len(answer)-1:
        answer = answer[:len(answer)-1]
    print(answer)

    # 7단계
    if len(answer) <= 2:
        # 마지막 값
        tmp = answer[-1]
        while len(answer) < 3:
            answer += tmp   # 여기에서 3 이 되니까..

    return answer

#n = "...!@BaT#*..y.abcd efghijklm"
n = "=.="

re = solution(n)
print(re)


'''
[규칙]
1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
     만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.

[기존]
def solution(new_id):
    answer = ''
    answer = new_id.lower()
    연습 = ""
    for ch in answer:
        if ch.isalnum() :
            연습 += ch
        elif ch == "-" or ch == "_" or ch == "." :
            연습 += ch

    idx = 연습.find("..")
    while idx > -1 :
        #print(idx)
        연습 = 연습.replace("..", ".")
        idx = 연습.find("..")
    #print(연습)

    #print(연습[0])
    if len(연습) >1 and 연습[0] == "."  :
        연습 = 연습[1:]
    elif len(연습) ==1 and 연습[0] == "." :
        연습 = ""    
    if len(연습) >1 and 연습[-1] == "." :
        연습 = 연습[:-1]
    elif  len(연습) ==1 and 연습[-1] == "." :
        연습 = ""          
    print(연습)
    if 연습 == "":
        연습 = "a"

    #print(len(연습) )
    연습 = 연습[:15]

    if 연습[-1] == ".":
        연습 = 연습[:-1]


    if len(연습) <= 2 :
        last = 연습[-1]
        #print(last)
        while len(연습) < 3 :
            연습 += last
    #print(연습)
    answer = 연습
    return answer
'''