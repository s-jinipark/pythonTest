
import pywinmacro as p
import time

print(p.get_mouse_position() )

#p.click((865, 232))

for i in range(20) :
    p.click((865, 232))
    time.sleep(1)
'''
구글에서 검색 한뒤 (ex 고양이)
(>) 버튼 위치에  마우스를 가져가
20번 누름
'''