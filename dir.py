"""出席者ファイルを取得する."""
import os


def search(target_path, search_text):
    for path, _, filenames in os.walk(target_path):
        for filename in filenames:
            file_path = os.path.join(path, filename)
            with open(file_path, encoding='utf-8') as f:
                if search_text in f.read():
                    print(filename)


if __name__ == '__main__':
    search('input', '出席')
