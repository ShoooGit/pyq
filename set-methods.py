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
