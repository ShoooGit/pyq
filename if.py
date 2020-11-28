import random

x = random.choice([3, 5, 8, 10])
print('x=' + str(x))

# xの値を判定
if x < 5:
    print('xは5より小さい')
elif x == 5:
    print('xは5と等しい')
elif 5 < x < 10:
    print('xは5より大きくて、10より小さい')
else:
    print('xは10以上')