
import pywinmacro as pw
#########################
# 02 마우스의 조작
#########################
# 1. 마우스 커서 위치 탐색
print( pw.get_mouse_position() )

'''
현재 창의 최소화 버튼의 위치 (1407, 51)
'''
# 2. 마우스 이동시키기
#pw.move_mouse((1407, 51))

# 3. 마우스 클릭하기
#pw.l_click()

'''
더블 클릭
for i in range(2) :
    pw.l_click()
    
[5. 더 쉬운 방법] 
location = pw.get_mouse_position() 
pw.click(location)  # 왼쪽 버튼 클릭
pw.right_click(location)  # 오른쪽 버튼 클릭
pw.double_click(location)  # 더블 클릭
'''

# 6. 드래그 앤 드롭 (Drag & Drop)
print( pw.get_mouse_position() )

'''
창을 이동 시켜 볼려고 마우스 위치를 뽑았다
(878, 60) -> (1220, 253)
타이틀바 위치 -> 우하향
'''
#pw.drag_drop((878, 60) , (1220, 253))

# 7. 스크롤 올리기
pw.mouse_upscroll()

# 8. 스크롤 내리기
#pw.mouse_downscroll()

# 9. 특정 위치의 픽셀 정보 읽어오기
print(pw.get_color((675, 112)) )
# 예 > 0x413f3c

#########################
# 03 키보드의 조작
#########################
# 1. 화면에 글자 입력하기
#pw.typing('print(124)')

#2. (한글 입력)
#pw.type_in('한글')
'''
이 함수를 실행하면 입력받은 문자열을 클립보드에 저장했다가 붙여 넣는 과정이 실행된다
붙여 넣기가 막혀 있는 사이트 (암호 paste 막힘) 
=> 평소 typing() 함수 사용, 한글 입력할 때만 type_in()

3. 키보드의 버튼 누르기
pw.key_press_once("enter")

윈도우 버튼 누르기
pw.key_press_once('window')

4. 키보드 버튼 꾹 누르고 있기
pw.key_on(key)

pw.key_off(key)

5. 여러 키 누르기
pw.key_on("control")
pw.key_on("c")
pw.key_off("control")
pw.key_off("c")

6. 두개의 키를 동시에 누르는 방법
자주 쓰이는 키 조합
pw.ctrl_c()

pw.ctrl_v()

pw.ctrl_a() 등
'''

#pw.key_press_once('window')

#########################
# 04 화면의 정보 빠르게 뽑아오기
#########################

# 마우스 좌표 추적
position = pw.get_mouse_position()

# 마우스 좌표 출력
print('Your mouse position is ' + str(position))

# 마우스 좌표의 색상을 추출해서 출력
print('Color in hex is ' + str(pw.get_color(position)))
