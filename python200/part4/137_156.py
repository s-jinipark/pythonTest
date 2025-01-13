'''
137 텍스트 파일을 읽고 출력하기(read)
138 텍스트 파일을 한줄씩 읽고 출력하기 ① (readline)
139 텍스트 파일을 한줄씩 읽고 출력하기 ② (readlines)
140 화면에서 사용자 입력을 받고 파일로 쓰기(write)
141 텍스트 파일에 한줄씩 쓰기(writelines)
142 텍스트 파일 복사하기(read, write)
143 바이너리 파일 복사하기(read, write)
144 파일을 열고 자동으로 닫기(with~as)
145 파일의 특정 부분만 복사하기(seek, read, write)
146 파일 크기 구하기(ospathgetsize)
147 파일 삭제하기(osremove)
148 파일이름 바꾸기(osrename)
149 파일을 다른 디렉터리로 이동하기(osrename)
150 디렉터리에 있는 파일목록 얻기(oslistdir, globglob)
151 현재 디렉터리 확인하고 바꾸기(osgetcwd, oschdir)
152 디렉터리 생성하기(osmkdir)
153 디렉터리 제거하기(osrmdir)
154 하위 디렉터리 및 파일 전체 삭제하기(shutilrmtree)
155 파일이 존재하는지 체크하기(ospathexists)
156 파일인지 디렉터리인지 확인하기(ospathisfile, ospathisdir)
'''

print("-----------------------------------")
print("137 텍스트 파일을 읽고 출력하기(read)")
#f = open('stock_part4.txt', 'r')
f = open('stock_part4.txt', 'r', encoding='UTF-8')
data = f.read()
print(data)
f.close()

# UnicodeDecodeError: 'cp949' codec can't decode byte 0xeb in position 7: illegal multibyte sequence


print("-----------------------------------")
print("138 텍스트 파일을 한줄씩 읽고 출력하기 ① (readline)")
f = open('stock_part4.txt', 'r', encoding='UTF-8')
line_num = 1
line = f.readline()
while line :
    print('%d %s'%(line_num, line), end='')  # 읽어들인 한 줄에는 '\n' 이 포함되어 있으므로 ..
    line = f.readline()
    line_num += 1
f.close()


print("-----------------------------------")
print("139 텍스트 파일을 한줄씩 읽고 출력하기 ② (readlines)")
f = open('stock_part4.txt', 'r', encoding='UTF-8')
lines = f.readlines()
for line_num, line in enumerate(lines):
    print('%d %s'%(line_num+1, line), end='')
f.close()
# read() 와 마찬가지로 모든 내용을 한꺼번에 읽기 때문에
# 파일 크기가 매우 큰 경우 문제 발생 가능


print("-----------------------------------")
print("140 화면에서 사용자 입력을 받고 파일로 쓰기(write)")
# text = input('파일에 저장할 내용 입력 >')
# f = open('test.txt', 'w', encoding='UTF-8')
# f.write(text)
# f.close()

# f = open('test.txt', 'w')
# 한글 입력시 깨짐


print("-----------------------------------")
print("141 텍스트 파일에 한줄씩 쓰기(writelines)")
# count = 1
# data = []
# print('파일 저장 - 내용 없이 [Enter] ')
# while True:
#     text = input('[%d] 파일에 입력할 내용 입력 :'%count)
#     if text == '':
#         break
#     data.append(text+'\n')
#     count += 1
# #f = open('mydata.txt', 'w')
# f = open('mydata.txt', 'w', encoding='UTF=8')
# f.writelines(data)
# f.close()


print("-----------------------------------")
print("142 텍스트 파일 복사하기(read, write)")
f = open('stock_part4.txt', 'r', encoding='UTF-8')
h = open('stock_part4_copy.txt', 'w', encoding='UTF-8')

data = f.read()
h.write(data)

f.close()
h.close()

# 그냥하면 오류 남
# UnicodeDecodeError: 'cp949' codec can't decode byte 0xeb in position 7: illegal multibyte sequence


print("-----------------------------------")
print("143 바이너리 파일 복사하기(read, write)")
bufsize = 1024
f = open('test_blackpink.jpg', 'rb')
h = open('test_blackpink_copy.jpg', 'wb')

data = f.read(bufsize)
while data :
    h.write(data)
    data = f.read(bufsize)

f.close()
h.close()
'''
대용량 파일의 내용을 한 번에 읽고 쓰는 것은 
메모리 용량의 한계로 불가능할 때 있고, 성능적인 면에서도 효율적이지 못함

bufsize 는 1024 로 정의. 1KB 단위로 파일을 읽기 위해 정의
만약 파일을 256KB 단위로 읽고 싶은 경우엔 bufsize 를 256 * 1024 로 정의하면 됨
'''


print("-----------------------------------")
print("144 파일을 열고 자동으로 닫기(with~as)")
with open('stock_part4.txt', 'r', encoding='UTF-8') as f :
    for line_num, line in enumerate(f.readlines()) :
        print('%d %s'%(line_num+1, line), end='')


print("-----------------------------------")
print("145 파일의 특정 부분만 복사하기(seek, read, write)")
spos = 15
size = 500
# f = open('stock_part4.txt', 'r', encoding='UTF-8')
# h = open('stock_part4_part.txt', 'w', encoding='UTF-8')
f = open('stock_part4.txt', 'r')
h = open('stock_part4_part.txt', 'w')

f.seek(spos)
data = f.read(size)
h.write(data)

h.close()
f.close()

'''
encoding 'UTF-8' 로 하니 오류 남
  UnicodeDecodeError: 'utf-8' codec can't decode byte 0xbd in position 0: invalid start byte
그냥하면
  일부 한글 깨짐
'''


print("-----------------------------------")
print("146 파일 크기 구하기(ospathgetsize)")
from os.path import getsize

file1 = 'stock_part4.txt'
#file2 = 'D:\dev\workspaces\pycharm\python200\part4\test_blackpink.jpg'  # 오류
file2 = 'D:/dev/workspaces/pycharm/python200/part4/test_blackpink.jpg'
file_size1 = getsize(file1)
file_size2 = getsize(file2)
print(file_size1)
print(file_size2)


print("-----------------------------------")
print("147 파일 삭제하기(osremove)")
from os import remove

target_file = 'stock_part4_copy.txt'
#k = input('[%s]파일을 삭제하겠습니까? (y/n)'%target_file)
k = 'y'
if k == 'y':
    remove(target_file)
    print('[%s]파일을 삭제했습니다.'%target_file)


print("-----------------------------------")
print("148 파일이름 바꾸기(osrename)")
# from os import rename
#
# target_file = 'stock_part4.txt'
# newname = 'stock_part4.txt'
# rename(target_file, newname)
# print('[%s] -> [%s] 로 변경되었습니다.'%(target_file, newname))


print("-----------------------------------")
print("149 파일을 다른 디렉터리로 이동하기(osrename)")
from os import rename

target_file = 'stock_part4_part.txt'
#newpath = input('[%s] 를 이동할 디렉토리의 절대 경로 입력'%target_file)
newpath = 'D:/dev/workspaces/pycharm/python200/part4/temp'
# [WinError 3] 지정된 경로를 찾을 수 없습니다: ...
# 폴더 만들고 다시
# 한번 더 실행하면  [WinError 183] 파일이 이미 있으므로 만들 수 없습니다: ...

# if newpath[-1] == '/':
#     newname = newpath + target_file
# else :
#     newname = newpath + '/' + target_file
#
# try :
#     rename(target_file, newname)
#     print('[%s] -> [%s] 로 이동 되었습니다.' % (target_file, newname))
# except FileNotFoundError as e :
#     print(e)


print("-----------------------------------")
print("150 디렉터리에 있는 파일목록 얻기(oslistdir, globglob)")
import os, glob

folder = 'D:/dev/workspaces/pycharm/python200/part4'
file_list = os.listdir(folder)
print(file_list)

files = '*.txt'
file_list = glob.glob(files)
print(file_list)

'''
listdir() 은 인자로 입력된 경로에 존재하는 모든 파일과 디렉터리를 리스트로 리턴
glob() 는 인자로 입력된 조건이나 경로에 해당하는 파일들을 리스트로 리턴
  => 와일드카드(*) 사용가능
'''
print("-----------------------------------")
print("151 현재 디렉터리 확인하고 바꾸기(osgetcwd, oschdir)")
import os

pdir = os.getcwd(); print(pdir)
os.chdir('..'); print(os.getcwd())
os.chdir(pdir); print(os.getcwd())


print("-----------------------------------")
print("152 디렉터리 생성하기(osmkdir)")
#newfolder = input('새로 생성할 디렉터리 이름 ?')
newfolder = 'temp2'
try:
    os.mkdir(newfolder)
    print('[%s] 디렉토리를 새로 생성했습니다.'%newfolder)
except Exception as e:
    print(e)

# 2회 실행 시
# [WinError 183] 파일이 이미 있으므로 만들 수 없습니다: 'temp2'


print("-----------------------------------")
print("153 디렉터리 제거하기(osrmdir)")
target_folder = 'temp2'
try :
    os.rmdir(target_folder)
    print('[%s] 디렉토리를 삭제했습니다.'%target_folder)
except Exception as e :
    print(e)


print("-----------------------------------")
print("154 하위 디렉터리 및 파일 전체 삭제하기(shutilrmtree)")
import shutil

target_folder =  'D:/dev/workspaces/pycharm/python200/part4/temp3'

try :
    shutil.rmtree(target_folder)
    print('삭제 했음')
except Exception as e :
    print(e)

# 없으면 [WinError 3] 지정된 경로를 찾을 수 없습니다:

print("-----------------------------------")
print("155 파일이 존재하는지 체크하기(ospathexists)")
from os.path import exists

dir_name = 'temp4'
if not exists(dir_name) :
    os.mkdir(dir_name)
    print('생성 했음')
else :
    print('이미 존재')


print("-----------------------------------")
print("156 파일인지 디렉터리인지 확인하기(ospathisfile, ospathisdir)")
from os.path import exists, isdir, isfile

files = os.listdir()
for file in files :
    if isdir(file):
        print('DIR : %s'%file)

for file in files:
    if isfile(file) :
        print('FILE : %s'%file)
