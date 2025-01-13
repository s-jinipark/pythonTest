
# 신규 아이디 추천

def solution(new_id):
    answer = ''
    # 1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
    # 2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
    # 3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
    # 4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
    # 5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
    # 6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
    #     만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
    # 7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.

    answer = new_id.lower()
    tmp = ""
    for ch in answer:
        if ch.isalnum() :
            #print("1 > " + ch)
            tmp += ch
        elif ch == "-" or ch == "_" or ch == "." :
        # elif ch == "-" or ch == "_" or  "." :  #-> 마지막 부분 코딩 잘못함
            #print("2 > " + ch)
            tmp += ch

    idx = tmp.find("..")
    while idx > -1 :
        print(idx)
        tmp = tmp.replace("..", ".")
        idx = tmp.find("..")
    print("=>" +tmp)

    #print(tmp[0])
    if len(tmp) >1 and tmp[0] == "."  :
        tmp = tmp[1:]
    elif len(tmp) ==1 and tmp[0] == "." :
        tmp = ""    
    if len(tmp) >1 and tmp[-1] == "." :
        tmp = tmp[:-1]
    elif  len(tmp) ==1 and tmp[-1] == "." :
        tmp = ""          
    print(tmp)
    if tmp == "":
        tmp = "a"

    #print(len(tmp) )
    if len(tmp) >16:
        tmp = tmp[:15]

    print(">" + tmp)
    if tmp[-1] == ".":
        tmp = tmp[:-1]

    print(len(tmp) )
    #tmp = "ab"
    if len(tmp) <= 2 :
        last = tmp[-1]
        print(last)
        while len(tmp) < 3 :
            tmp += last
    print(tmp)
    answer = tmp
    return answer

#id = "...!@BaT#*..y.abcdefghijklm"
id = "=.="
print( solution(id) )

