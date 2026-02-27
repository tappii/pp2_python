from datetime import datetime, timedelta, timezone

def parse_moment(s):
    dt_str, tz_str = s.rsplit(' ', 1)
    dt = datetime.strptime(dt_str, "%Y-%m-%d %H:%M:%S")
    sign = 1 if tz_str[3] == '+' else -1
    hours = int(tz_str[4:6])
    minutes = int(tz_str[7:9])
    offset = timezone(timedelta(hours=sign*hours, minutes=sign*minutes))
    return dt.replace(tzinfo=offset).astimezone(timezone.utc)

start = parse_moment(input().strip())
end = parse_moment(input().strip())

duration_seconds = int((end - start).total_seconds())
print(duration_seconds)