from pathlib import Path

p = Path('input')
new_p =  p / 'sub' / 'test.txt'
print('new_p:', new_p)  # パスの表示: input/sub/test.txt
print('new_p.exists():', new_p.exists())  # パスの存在確認: True
print('new_p.is_file():', new_p.is_file())  # パスがファイルかどうか確認: True
