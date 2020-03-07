import sys
import psutil
import os

result = {}
print(sys.argv[0])
if sys.argv[1] == "mem":
    print(psutil.cpu_percent())
elif  sys.argv[1] == "-cpu":
    cpuStat =  psutil.cpu_times_percent()
    result["system.cpu.idle"] = cpuStat[3]
    result["system.cpu.user"] =  cpuStat[0]
    result["system.cpu.guest"] =  cpuStat[8]
    result["system.cpu.iowait"] =  cpuStat[3]
    result["system.cpu.stolen"] =  cpuStat[6]
    result["system.cpu.system"] =  cpuStat[2]
    for k, v in result.items():
        print("{} {:.2f}".format(k, v))    
else:
    print('Unknown arguments')