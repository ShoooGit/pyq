items = {'art'}
print("items:", items)

# 1要素を削除
result = items.pop()
print("items.pop():", result)
print("items:", items)

# リストを追加
items.update(['egg', 'fog'])
print("items.update(['egg', 'fog'])")
print("items:", items)

# 全削除
items.clear()
print("items.clear()")
print("items:", items)

# 追加
items.add('doll')
print("items.add('doll')")
print("items:", items)

# 削除
items.remove('doll')
print("items.remove('doll')")
print("items:", items)

items = {3, 4}
print("items:", items)

# 共通する要素がないか
result1 = items.isdisjoint({1, 2})
print("items.isdisjoint({1, 2}):", result1)

# 部分集合か
result2 = items.issubset({1, 3, 4})
print("items.issubset({1, 3, 4}):", result2)

# 引数が部分集合か
result3 = items.issuperset({4})
print("items.issuperset({4}):", result3)

s1 = set('ab')
s2 = set('bc')
print("s1:", s1)
print("s2:", s2)

# 差集合
result1 = s1.difference(s2)
print("s1.difference(s2):", result1)

# 積集合
result2 = s1.intersection(s2)
print("s1.intersection(s2):", result2)

# 対称差
result3 = s1.symmetric_difference(s2)
print("s1.symmetric_difference(s2):", result3)

# 和集合
result4 = s1.union(s2)
print("s1.union(s2):", result4)