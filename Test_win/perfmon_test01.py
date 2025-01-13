import winstats

# https://pypi.org/project/winstats/

# optional
import locale
locale.setlocale(locale.LC_ALL, '')
fmt = lambda n: locale.format('%d', n, True)

# --------------------
# Memory Stats:

meminfo = winstats.get_mem_info()
#print '    Total: %s b' % fmt(meminfo.TotalPhys)
#print '    usage: %s%%' % fmt(meminfo.MemoryLoad)
#print
print("    Total: %s b" % (meminfo.TotalPhys) )
print("    usage: %s%%" % (meminfo.MemoryLoad) )

# --------------------
# Performance Stats:

pinfo = winstats.get_perf_info()
#print '    Cache: %s p' % fmt(pinfo.SystemCache)
#print '    Cache: %s b' % fmt(pinfo.SystemCacheBytes)
print("    Cache: %s p" % (pinfo.SystemCache) )
print("    Cache: %s b" % (pinfo.SystemCacheBytes) )

# --------------------
# Disk Stats:

drives = winstats.get_drives()
drive = drives[0]
fsinfo = winstats.get_fs_usage(drive)
vinfo = winstats.get_vol_info(drive)

#print '    Disks:', ', '.join(drives)
#print '    %s:\\' % drive
#print '        Name:', vinfo.name
#print '        Type:', vinfo.fstype
#print '        Total:', fmt(fsinfo.total)
#print '        Used: ', fmt(fsinfo.used)
#print '        Free: ', fmt(fsinfo.free)
print("    Disks:", ", ".join(drives) )
