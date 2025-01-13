
#사용자 입력 받기

langs = ["한국어", "English"]
for i, l in enumerate(langs, start=1):
    print("{}. {}".format(i, l))

while True:
    sel = input("언어를 선택하세요.>")

    if not sel.isnumeric():
        continue
    
    sel = int(sel)
    if 0 < sel < 3:
        break

print("사용자가 선택한 언어는 {} 입니다.".format(langs[sel-1]))


