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

items = [1]
print("items:", items)

# 末尾にリストを追加
items.extend([2, 5, 3, 4])
print("items.extend([2, 5, 3, 4])")
print("items:", items)

# 要素を削除
items.remove(3)
print("items.remove(3)")
print("items:", items)

# 末尾を削除して取得
result = items.pop()
print("items.pop():", result)
print("items:", items)

# 5の位置を探索
result = items.index(5)
print("items.index(5):", result)

# コピー
items2 = items.copy()
print("items2 = items.copy()")

# 逆順でソート
items.sort(reverse=True)
print("items.sort(reverse=True)")
print("items:", items)
print("items2:", items2)
