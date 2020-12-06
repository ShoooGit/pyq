from pathlib import Path

p = Path('input')
new_p =  p / 'sub' / 'test.txt'
print('new_p:', new_p)  # パスの表示: input/sub/test.txt
print('new_p.exists():', new_p.exists())  # パスの存在確認: True
print('new_p.is_file():', new_p.is_file())  # パスがファイルかどうか確認: True

print('new_p.name:', new_p.name)  # ファイル名の取得: test.txt
print('new_p.suffix:', new_p.suffix)  # 拡張子の取得: .txt
print('new_p.stem:', new_p.stem)  # ファイル名の拡張子以外の部分の取得: test
print('new_p.parts:', new_p.parts)  # パスを分解したものの取得: ('input', 'sub', 'test.txt')
print('new_p.parent:', new_p.parent)  # 親ディレクトリーの取得: input/sub