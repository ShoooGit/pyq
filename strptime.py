from datetime import datetime
from datetime import timedelta

# 文字列の日付
meeting_day = '2016-08-01'
# 文字列から日付時刻の作成
the_day = datetime.strptime(meeting_day, '%Y-%m-%d')
# 100日後の日付時刻の作成
after_100days = the_day + timedelta(days=100)
# 100日後の表示
print(after_100days.date())
