# データをまとめる空の辞書を作る
health_result = {}

# 要素の追加
health_result['名前'] = '佐藤'
health_result['年齢'] = 35
health_result['体重'] = 60
health_result['身長'] = 170
health_result['視力'] = 2.0

# 身長、体重の表示
print(health_result['名前'], 'さんの', sep='')
print('身長は', health_result['身長'], 'cmです', sep='')
print('体重は', health_result['体重'], 'kgです', sep='')