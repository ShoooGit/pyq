from datetime import datetime

one_day = datetime(2015, 12, 31, 23, 55, 2)

str_datetime = f'{one_day = :%Y-%m-%d %H:%M:%S}'
print(str_datetime)
print(one_day.date(), one_day.time())
