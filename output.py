output_rows = []

with open('./input/books.csv', encoding='utf-8') as f:
    for row in f:
        columns = row.strip().split(',')
        purpose = columns[2]  # 会議室の利用目的

        if purpose == 'Python-勉強会':
            output_rows.append(row)

# ファイル'output/book_python.csv'へ書き込む
with open('output/book_python.csv', 'w', encoding='utf-8') as wf:
    for row in output_rows:
        wf.write(row)