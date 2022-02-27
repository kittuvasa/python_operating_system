import shutil
import psutil #dependency, post-built

def check_disk_usage(disk):
    usage = shutil.disk_usage(disk)
    print( ">free space {:.1f}GB".format(usage.free/(1024*1024*1024)))
    if usage.free/usage.total*100 > 20:
        print("free space ✔ ")
    else:
        print("Alert ❌ ")
    
def u_processor_usage():
    usage = psutil.cpu_percent(1)
    if usage<75:
        print("check cpu usage ✔")
    else:
        print("usage limit ❌")

def check_sys_health():
    check_disk_usage("/")
    u_processor_usage()
#
