def func(foo, bar=None):
    print('foo =', foo)
    print('bar =', bar)
    print()


func(1, 2)  # 位置引数
func(3)  # 位置引数
func(foo=4)  # キーワード引数
func(5, bar=6)  # 位置引数とキーワード引数
func(bar=8, foo=7)  # キーワード引数（順番変更）