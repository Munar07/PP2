from datetime import datetime, timedelta, timezone
import math

def parse_dt(s):
    date_str, tz_str = s.split()
    dt = datetime.strptime(date_str, "%Y-%m-%d")
    sign = 1 if tz_str[3] == '+' else -1
    hours = int(tz_str[4:6])
    minutes = int(tz_str[7:9])
    tz = timezone(timedelta(hours=sign*hours, minutes=sign*minutes))
    return dt.replace(tzinfo=tz)

def is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

birth = parse_dt(input().strip())
current = parse_dt(input().strip())

b_month = birth.month
b_day = birth.day

current_utc = current.astimezone(timezone.utc)

year = current_utc.year
while True:
    day = 28 if b_month == 2 and b_day == 29 and not is_leap(year) else b_day
    candidate_local = datetime(year, b_month, day, tzinfo=birth.tzinfo)
    candidate_utc = candidate_local.astimezone(timezone.utc)
    if candidate_utc >= current_utc:
        break
    year += 1

# используем math.ceil для округления дробного дня вверх
delta_days = math.ceil((candidate_utc - current_utc).total_seconds() / (24*3600))
print(delta_days)
