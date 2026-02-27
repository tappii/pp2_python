from datetime import datetime, timedelta, timezone

def parse_date(s):
    date_str, tz_str = s.split()
    dt = datetime.strptime(date_str, "%Y-%m-%d")
    sign = 1 if tz_str[3] == '+' else -1
    hours = int(tz_str[4:6])
    minutes = int(tz_str[7:9])
    offset = timezone(timedelta(hours=sign*hours, minutes=sign*minutes))
    return dt.replace(tzinfo=offset)

def is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

birth = parse_date(input().strip())
current = parse_date(input().strip())

b_month, b_day = birth.month, birth.day
c_year = current.year

if b_month == 2 and b_day == 29 and not is_leap(c_year):
    b_day = 28

next_birthday = birth.replace(year=c_year, month=b_month, day=b_day)
next_birthday_utc = next_birthday.astimezone(timezone.utc)
current_utc = current.astimezone(timezone.utc)

if next_birthday_utc < current_utc:
    c_year += 1
    b_day = birth.day
    if birth.month == 2 and birth.day == 29 and not is_leap(c_year):
        b_day = 28
    next_birthday = birth.replace(year=c_year, month=birth.month, day=b_day)
    next_birthday_utc = next_birthday.astimezone(timezone.utc)

diff_seconds = (next_birthday_utc - current_utc).total_seconds()
days_left = int((diff_seconds + 86399) // 86400)  # ceiling division to count partial day as 1
print(days_left)