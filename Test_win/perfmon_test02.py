import winstats
import wmi 

# wmi_conn = wmi.WMI()
# #proc_list = wmi_conn.Win32_Service(Name=service_name)
# proc_list = wmi_conn.Win32_Service(Name="Server")
# print(proc_list)

#Perfmon - Performance Counters:

# take a second snapshot 100ms after the first:
#usage = winstats.get_perf_data(r'\Processor(_Total)\% Processor Time',
#                               fmts='double', delay=100)
#print ("    CPU Usage: %.02f %%" % usage )

# usage = winstats.get_perf_data(r'\.NET CLR Memory(CodeHelper)\# GC Handles',
#                                fmts='double', delay=100)
# print ("    >> : %.02f " % usage )

COUNTERS = [
    (r'\.NET CLR Memory(powershell#1)\Process ID',
     'asp.net.application.restarts',
     'GAUGE'),
    (r'\.NET CLR Memory(powershell#2)\Process ID',
     'asp.net.requests.current',
     'GAUGE'),
    (r'\.NET CLR Memory(powershell)\Process ID',
     'asp.net.request_execution_time',
     'GAUGE'),
]

COUNTERS2 = [
    (r'\.NET CLR Memory($WH$)\Gen 0 heap size',
     'asp.net.application.restarts',
     'GAUGE'),
    (r'\.NET CLR Memory($WH$)\# Bytes in all Heaps',
     'asp.net.requests.current',
     'GAUGE'),
    (r'\.NET CLR Memory($WH$)\% Time in GC',
     'asp.net.request_execution_time',
     'GAUGE'),
]

for counter, metric, vtype in COUNTERS:
    try:
        counter_value = winstats.get_perf_data(counter, delay=100)

    except Exception as e:
        print(e)
        continue
    value = counter_value[0]
    if value == 564 :
        print("ok")
    print(metric)


test = 'powershell'

for counter, metric, vtype in COUNTERS2:
    try:
        print(counter)
        counter= counter.replace("$WH$", test)
        print(counter)
        counter_value = winstats.get_perf_data(counter, delay=100)

    except Exception as e:
        print(e)
        continue
    value = counter_value[0]

    print(value)


# query multiple at once:
counters = [ r'\Paging File(_Total)\% Usage', r'\Memory\Available MBytes']
results = winstats.get_perf_data(counters, fmts='double large'.split())
print ("    Pagefile Usage: %.2f %%, Mem Avail: %s MB" % results )




