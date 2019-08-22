#1408

time = raw_input()
mstart = raw_input()

def timeTosec(t):
    li=t.split(':')
    totalSec = int(li[0])*3600+int(li[1])*60+int(li[2])
    return totalSec

def secTotime(s):
    h = s/3600
    m = (s%3600)/60
    s = (s%3600)%60
    
    return str(h)+":"+str(m)+":"+str(s)

def remainTime(time,mstart):
    ts = timeTosec(time)
    ms = timeTosec(mstart)
    if ts<ms:
        return secTotime(ms-ts)
    else:
        return secTotime(86400-(ts-ms))

print(remainTime(time,mstart))