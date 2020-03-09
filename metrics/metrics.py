import sys
import psutil
import os

# print(psutil.cpu_times_percent())
def mem():
    svmem = psutil.virtual_memory()
    result = {}
    result["virtual total"] = svmem[0]
    result["virtual used"] = svmem[3]
    result["virtual free"] = svmem[4]
    result["virtual shared"] = svmem[9]
    sswap = psutil.swap_memory()
    result["swap total"] = sswap[0]
    result["swap used"] = sswap[1]
    result["swap free"] = sswap[2]

    return result

def cpu():
    cpuStat =  psutil.cpu_times_percent(interval=1)
    result = {}
    result["system.cpu.idle"] = cpuStat[3]
    result["system.cpu.user"] =  cpuStat[0]
    result["system.cpu.guest"] =  cpuStat[8]
    result["system.cpu.iowait"] =  cpuStat[4]
    result["system.cpu.stolen"] =  cpuStat[6]
    result["system.cpu.system"] =  cpuStat[2]
  
    return result

if sys.argv[1] == "mem":
    for k, v in mem().items():
        print("%s %s" % (k, v))
    
elif  sys.argv[1] == "cpu":
    for k, v in cpu().items():
        print("{} {:.2f}".format(k, v))    
else:
    print('Unknown arguments')
