mail = """フットサル大会への参加ありがとうございました: %X%さんへ

この度はフットサル大会への参加ありがとうございました。
参加者のみなさんからは楽しかった、いい息抜きになったと意見をいただいております。
%X%さんはどうだったでしょうか？
是非感想をお聞かせください。
今回のフットサルが好評だったため、次回の予定も決まりました。
来月13日に行います。詳しくはまた連絡いたします。
%X%さんの参加を楽しみに待っています。
"""

member = ["木田", "山下", "山口", "高橋", "加藤", "鈴木", "吉田", "大山", "町田"]

for name in member:
    print(mail.replace("%X%", name))