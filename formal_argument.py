def func(foo, bar=None):
    print('foo =', foo)
    print('bar =', bar)
    print()


func(1, 2)  # 位置引数
func(3)  # 位置引数
func(foo=4)  # キーワード引数
func(5, bar=6)  # 位置引数とキーワード引数
func(bar=8, foo=7)  # キーワード引数（順番変更）

def func1(arg, *, kw_only1, kw_only2):
    print('arg =', arg)
    print('kw_only1 =', kw_only1)
    print('kw_only2 =', kw_only2)
    print()


func1(1, kw_only1=2, kw_only2=3)  # 定義と同じ順番
func1(1, kw_only2=3, kw_only1=2)  # 順番は変えても良い
func1(kw_only2=3, kw_only1=2, arg=1)  # 順番は変えても良い


def func2(arg, *, kw_only1=2, kw_only2):
    print('arg =', arg)
    print('kw_only1 =', kw_only1)
    print('kw_only2 =', kw_only2)
    print()


func2(1, kw_only2=3)  # デフォルト値は省略可