import random
# ベットする数
user_selected = 8
row = 1

for num in range(1,101):
    if user_selected == random.randint(1,10):
        print(row, "回目に当たり")
    row += 1