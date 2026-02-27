from datetime import datetime, timedelta, timezone

def parse_moment(s):
    date_str, tz_str = s.split()
    dt = datetime.strptime(date_str, "%Y-%m-%d")
    sign = 1 if tz_str[3] == '+' else -1
    hours = int(tz_str[4:6])
    minutes = int(tz_str[7:9])
    offset = timezone(timedelta(hours=sign*hours, minutes=sign*minutes))
    dt = dt.replace(tzinfo=offset)
    return dt.astimezone(timezone.utc)

dt1 = parse_moment(input().strip())
dt2 = parse_moment(input().strip())

diff_seconds = abs((dt1 - dt2).total_seconds())
full_days = int(diff_seconds // 86400)
print(full_days)