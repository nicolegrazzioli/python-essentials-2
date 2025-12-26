from datetime import date
import time

# today = date.today()

# print("Today:", today) # 2025-12-25
# print("Year:", today.year) # 1 (const MINYEAR) <= year <= 9999 (const MAXYEAR)
# print("Month:", today.month) # 1 <= month <= 12
# print("Day:", today.day) # 1 <= day <= [último dia do mês do ano]

# # CRIAR OBJETO DATE
# my_date = date(2019, 11, 24)

# CRIAR DATE POR TIMESTAMP

# timestamp = time.time()
# print("Timestamp: ", timestamp) #1766701...

# d = date.fromtimestamp(timestamp)
# d = d.replace(month=10, day=26)
# print("Date: ", d) #2025-12-25
# print(d.weekday())

# time(hour, minute, second, microsecond, tzinfo, fold)
# 0 <= hour < 23
# 0 <= minute < 59
# 0 <= second < 59
# 0 <= microsecond < 1000000
# tzinfo = objeto da subclasse tzinfo ou None (default)
# fold (zonas de tempo) = 0 (default) ou 1 

# timestamp = 1572879180
# print(time.ctime(timestamp)) # Mon Nov 4 14:53:00 2019
# print(time.ctime()) # Thu Dec 25 20:11:59 2025

# time.struct_time:
#     tm_year   # year
#     tm_mon    # month (value from 1 to 12)
#     tm_mday   # day of the month (value from 1 to 31)
#     tm_hour   # hour (value from 0 to 23)
#     tm_min    # minute (value from 0 to 59)
#     tm_sec    # second (value from 0 to 61 )
#     tm_wday   # weekday (value from 0 to 6)
#     tm_yday   # year day (value from 1 to 366)
#     tm_isdst  # her daylight saving time applies (1 – yes, 0 – no, -1 – it isn't known)
#     tm_zone   # timezone name (value in an abbreviated form)
#     tm_gmtoff # offset east of UTC (value in seconds)

# timestamp = 1572879180
# # retorna objeto em UTC, atributo tm_isdst == 0
# print(time.gmtime(timestamp)) # time.struct_time(tm_year=2019, tm_mon=11, tm_mday=4, tm_hour=14, tm_min=53, tm_sec=0, tm_wday=0, tm_yday=308, tm_isdst=0)
# # retorna tempo local
# print(time.localtime(timestamp)) # time.struct_time(tm_year=2019, tm_mon=11, tm_mday=4, tm_hour=14, tm_min=53, tm_sec=0, tm_wday=0, tm_yday=308, tm_isdst=0)

# timestamp = 1572879180
# st = time.gmtime(timestamp)

# print(time.asctime(st)) #Mon Nov 4 14:53:00 2019
# print(time.mktime((2019, 11, 4, 14, 53, 0, 0, 308, 0))) #1572879180.0
    
# # tupla
# # 2019 => tm_year
# # 11 => tm_mon
# # 4 => tm_mday
# # 14 => tm_hour
# # 53 => tm_min
# # 0 => tm_sec
# # 0 => tm_wday
# # 308 => tm_yday
# # 0 => tm_isdst

# datetime(year, month, day, hour, minute, second, microsecond, tzinfo, fold)
# 1 (const MINYEAR) <= year <= 9999 (const MAXYEAR)
# 1 <= month <= 12
# 1 <= day <= [último dia do mês do ano]
# 0 <= hour < 23
# 0 <= minute < 59
# 0 <= second < 59
# 1 <= microsecond < 1000000
# tzinfo = objeto da subclasse tzinfo ou None (default)
# fold (zonas de tempo) = 0 (default) ou 1 
# EX:
# Datetime: 2019-11-04 14:53:00
# Date: 2019-11-04
# Time: 14:53:00

# from datetime import datetime

# print("today:", datetime.today()) # today: 2025-12-25 23:53:22.138194
# print("now:", datetime.now()) # now: 2025-12-25 23:53:22.140864
# print("utcnow:", datetime.utcnow()) # utcnow: 2025-12-25 23:53:22.141134

# from datetime import datetime

# dt = datetime(2020, 10, 4, 14, 55)
# print("Timestamp:", dt.timestamp()) # 1601823300.0

# from datetime import date, time, datetime

# d = date(2020, 1, 4)
# print(d.strftime('%d/%m/%Y')) # 04/01/2020

# t = time(14, 53)
# print(t.strftime("%H:%M:%S")) # 14::53:00

# dt = datetime(2020, 11, 4, 14, 53)
# print(dt.strftime("%y/%B/%d %H:%M:%S")) # 20/November/04 14:53:00
    
# import time

# timestamp = 1572879180
# st = time.gmtime(timestamp)

# # formata objeto struct_time
# print(time.strftime("%Y/%m/%d %H:%M:%S", st)) # 2019/11/04 14:53:00
# # formata hora atual
# print(time.strftime("%Y/%m/%d %H:%M:%S")) # 2025/12/25 21:09:57

# from datetime import datetime
# # 1o arg: data e hora como string
# # 2o arg: formato, pode dar ValueError
# print(datetime.strptime("2019/11/04 14:53:00", "%Y/%m/%d %H:%M:%S")) # 2019-11-04 14:53:00
    
# import time
# print(time.strptime("2019/11/04 14:53:00", "%Y/%m/%d %H:%M:%S")) # time.struct_time(tm_year=2019, tm_mon=11, tm_mday=4, tm_hour=14, tm_min=53, tm_sec=0, tm_wday=0, tm_yday=308, tm_isdst=-1)

from datetime import date
from datetime import datetime

d1 = date(2020, 11, 4)
d2 = date(2019, 11, 4)

print(d1 - d2) # 366 days, 0:00:00

dt1 = datetime(2020, 11, 4, 0, 0, 0)
dt2 = datetime(2019, 11, 4, 14, 53, 0) # especificou o tempo incluso

print(dt1 - dt2) # 365 days, 9:07:00

# argumentos do construtor (opcionais, default = 0): days, seconds, microseconds, milliseconds, minutes, hours, weeks
delta = timedelta(weeks=2, days=2, hours=3)
print(delta) # 16 days, 3:00:00 --> converte argumento weeks para dias (14d) + argumento days (2d)
print("Days:", delta.days) # 16
print("Seconds:", delta.seconds) # 10800 (3h -> sec)
print("Microseconds:", delta.microseconds) # 0 (milisec -> microsec)

delta2 = delta * 2
print(delta2) # 32 days, 4:00:00

d = date(2019, 10, 4) + delta2 # objetos datetime + dias e horas = objeto timedelta
print(d) # 2019-11-05

dt = datetime(2019, 10, 4, 14, 53) + delta2
print(dt) # 2019-11-05 18:53:00