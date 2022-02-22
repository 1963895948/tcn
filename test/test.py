import datetime
import data

now = datetime.datetime.strptime('2020-01-01', "%Y-%m-%d")
date = now + datetime.timedelta(days=31)
print(date)
