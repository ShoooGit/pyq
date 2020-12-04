items = ['art', 'box', 'cup']
print("items:", items)

# 末尾に追加
items.append('doll')
print("items.append('doll')")
print("items:", items)

# 途中に追加
items.insert(2, 'doll')
print("items.insert(2, 'doll')")
print("items:", items)

# 計測
result = items.count('doll')
print("items.count('doll'):", result)

# 位置0の要素を削除
del items[0]
print("del items[0]")
print("items:", items)

# 反転
items.reverse()
print("items.reverse()")
print("items:", items)

# 全削除
items.clear()
print("items.clear()")
print("items:", items)
