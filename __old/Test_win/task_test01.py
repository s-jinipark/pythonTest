import re
import subprocess

def get_processes_running():
    # 영어일때는 `ignore` 인자 없어도 됨  
    tasks = subprocess.check_output(['tasklist']).decode('cp949', 'ignore').split("\r\n")
    p = []
    for task in tasks:
        m = re.match("(.+?) +(\d+) (.+?) +(\d+) +(\d+.* K).*",task)
        if m is not None:
            p.append({"image":m.group(1),
                        "pid":m.group(2),
                        "session_name":m.group(3),
                        "session_num":m.group(4),
                        "mem_usage":m.group(5)
                        })
    return p
#print("t")
print(get_processes_running() )

# http://blog.ju-ing.com/posts/How-to-get-tasklist-in-python/

#D:\dev\workspaces\python\Test\dist>where pyinstaller
# C:\Users\jini\anaconda3\Scripts\pyinstaller.exe