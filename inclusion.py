from pprint import pprint

log = """\
1/1 晴れ
1/2 晴れ
1/3 曇り
1/4 雨
1/5 雨
1/6 曇り
1/7 晴れ
"""

loglist = [s.split() for s in log.splitlines()]
print('loglist:')
pprint(loglist)
loglist2 = [it for it in loglist if '晴れ' in it]  # ここを修正してください
print('loglist2:', loglist2)
