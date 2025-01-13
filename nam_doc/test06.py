
#유니코드와 인코딩

#유니코드를 저장하는 방식 -> 인코딩

# vs code 에서 '가' 를 저장한 뒤 hexdump 로 보면
#  
#   Offset: 00 01 02 03 04 05 06 07 08 09 0A 0B 0C 0D 0E 0F 	
# 00000000: EA B0 80                                           j0.
# (탐색기 - 속성 -> 3바이트)


# 메모장에서 '가' 저장 후 hexdump 로 ...
#   Offset: 00 01 02 03 04 05 06 07 08 09 0A 0B 0C 0D 0E 0F 	
# 00000000: B0 A1                                              0!
# (탐색기 - 속성 -> 2바이트)


# 메모장에서 '가' 저장 (+ UTF-8 로) 후 hexdump 로 ...
#   Offset: 00 01 02 03 04 05 06 07 08 09 0A 0B 0C 0D 0E 0F 	
# 00000000: EF BB BF EA B0 80                                  o;?j0.
# (탐색기 - 속성 -> 6바이트)
# BOM : Byte Order Mark
# 파일이 어떤 인코딩으로 저장되었는지를 나타내는 하나의 사인


# file = open("utf8.txt", mode="r")
# print(file.read().decode("utf-8"))
# file.close()

# Traceback (most recent call last):
#   File "test06.py", line 28, in <module>
#     print(file.read().decode("utf-8"))
# UnicodeDecodeError: 'cp949' codec can't decode byte 0x80 in position 2: incomplete multibyte sequence


file = open("utf8.txt", mode="r", encoding="utf-8")
print(file.read())
file.close()

