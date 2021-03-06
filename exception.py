from string import ascii_uppercase

ALLOW_CHARS = ' ' + ascii_uppercase  # ' ABCD....XYZ'


def encrypt(value):
    """文字列を受取り、暗号化して数字列を返します

    :param str value: 暗号化の対象文字列
    :return: 数字のリスト
    :except ValueError: 予定外の文字がvalueに含まれている場合
    """
    nums = []  # 返値のリスト
    for c in value:  # 文字列を1文字ずつ取り出してループ
        n = ALLOW_CHARS.index(c.upper())  # 1文字を大文字にして、ALLOW_CHARSの何番目か調べる
        nums.append(n)  # 何番目かを返値のリストに追加
    return nums


def send_data(nums):
    """将来的にはデータを送りたいけれど今はプリントするだけ"""
    print(*nums)


def input_loop():
    while True:
        value = input('文章を入力してください[A-Z,Space]:')
        try:
            nums = encrypt(value)
        except ValueError:
            print(value, 'はローマ字またはスペースではありません')
        else:
            send_data(nums)


def main():
    input_loop()


if __name__ == '__main__':
    main()