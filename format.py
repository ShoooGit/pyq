card = """\
株式会社ビープラウド
{job_title}
{name}
MAIL: {mail}
TEL: 03-9999-9999 FAX: 03-9999-9998 内線: {extension}
URL: https://www.beproud.jp
"""

# この下に処理を記述します
sato_card = card.format(name='佐藤太郎',
                        job_title='エンジニア',
                        mail='taro@beproud.jp',
                        extension='1234')

print(sato_card)