import os
import glob

#entries = os.scandir(r'W:\01.수주PRM\00. 진단결과\2022')

#print(type(entries))
# 출력 => <class 'nt.ScandirIterator'>

base_dir = r'W:\01.수주PRM\00. 진단결과\2022'
# with os.scandir(base_dir) as entries :
#     for entry in entries :
#         print(entry.name)
#         # confirm_dir = "W:/01.수주PRM/00. 진단결과/2022" + entry.name + "/4. Confirm*/4.2 ARB 자료*/*.xls"
#         # print(confirm_dir)
#         # for filename in glob.glob(confirm_dir):
#         #     print(filename)
#         file_list = glob.glob(f"{base_dir}/4*/4.2*/*.xlsx")
#         print(file_list)


# [파이썬/Python] 모든 하위 디렉토리 탐색, 특정 확장자 찾기
# for (path, dir, files) in os.walk(base_dir):
#     for filename in files:
#         ext = os.path.splitext(filename)[-1]
#         if ext == '.xlsx':
#             print("%s/%s" % (path, filename))


# import glob
# # '*'는 임의 길이의 모든 문자열을 의미한다.
# print(glob.glob('W:/01.수주PRM/00. 진단결과/2023/*.txt'))


