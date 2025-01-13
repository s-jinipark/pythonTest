import psutil
tasklist = []
for proc in psutil.process_iter():
    try:
        tasklist.append({'pid': proc.name(), 'name': proc.pid})
    except:
        pass
print(tasklist)


# https://www.python2.net/questions-455955.htm

