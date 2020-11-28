# ファイルinput/telephone.csvの内容を表示しましょう。
with open('input/telephone.csv', encoding='utf-8') as f:
    for row in f:
        print(row.rstrip())