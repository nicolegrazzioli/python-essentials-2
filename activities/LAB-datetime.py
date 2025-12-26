"""objeto datetime 
november 4, 2020, 14:53:00

Output
ok 2020/11/04 14:53:00
ok 20/November/04 14:53:00 PM
ok Wed, 2020 Nov 04
ok Wednesday, 2020 November 04
Weekday: 3
Day of the year: 309
Week number of the year: 44
"""

from datetime import datetime, date
dt = datetime(2020, 11, 4, 14, 53)

print(dt.strftime("%Y/%m/%d %H:%M:%S"))
print(dt.strftime("%y/%B/%d %H:%M:%S %p"))
print(dt.strftime("%a, %Y %b %d"))
print(dt.strftime("%A, %Y %B %d"))
print("Weekday:", dt.isoweekday())
print("Day of the year:", dt.strftime("%j")) 
print("Week number of the year:", dt.strftime("%U")) 