import time
print("current time in sec:",time.time())
print("current time:",time.ctime())
print("time after 30 sec:",time .ctime(time.time()+30))
t=time.localtime()
print("time:",t)
print("time-current year:",t.tm_year)
print("time-current month:",t.tm_mon)
print("time-current day:",t.tm_mday)
print("time-current hour:",t.tm_hour)
print("time-current minute:",t.tm_min)
print("time-current sec:",t.tm_sec)
print("time-current week day:",t.tm_wday)
print("time-current year day:",t.tm_yday)