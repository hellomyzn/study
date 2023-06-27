import datetime
import time

now = datetime.datetime.now()
print(now)

print(now.strftime("%d/%m /%y - %H:%M:%S.%f"))

today = datetime.date.today()
print(today)
print(today.strftime("%d/%m/%y"))


t = datetime.time(hour=1, minute=10, second=5, microsecond=100)
print(t)
print(t.strftime("%H:%M:%S.%f"))


d = datetime.timedelta(weeks=1)
d = datetime.timedelta(days=1)
d = datetime.timedelta(hours=1)
d = datetime.timedelta(minutes=1)
d = datetime.timedelta(seconds=1)
d = datetime.timedelta(microseconds=1)
print(now-d)

print("###")
time.sleep(1)
print("###")
