# __init__メソッドを作ると、初期化する時に引数を任意に設定可能
class Human:
    def __init__(self, age=0, last_name='', first_name='', blood_type=''):
        self.age = age  # 年齢
        self.last_name = last_name  # 姓
        self.first_name = first_name  # 名前
        self.blood_type = blood_type  # 血液型


h1 = Human()
h2 = Human(33, '田中', '一郎', 'O')

print(h1.age, h1.last_name, h1.first_name, h1.blood_type)
print(h2.age, h2.last_name, h2.first_name, h2.blood_type)
