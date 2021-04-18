import datetime

date_str = "Sun 10 May 2015 13:54:36 -0700"

dt_str = date_str[:-5].strip()
dt_zone = int(date_str[-5:]) / 100
pattern = '%a %d %B %Y %H:%M:%S'

dt_obj = datetime.datetime.strptime(dt_str, pattern)
dt = dt_obj + datetime.timedelta(hours=dt_zone)
print(dt.strftime('%s'))
