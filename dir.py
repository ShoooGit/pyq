"""出席者ファイルを取得する."""
import os


def search(target_path, search_text):
    for filename in os.listdir(target_path):
        file_path = os.path.join(target_path, filename)
        if os.path.isfile(file_path):
            with open(file_path, encoding='utf-8') as f:
                if search_text in f.read():
                    print(filename)


if __name__ == '__main__':
    search('input', '出席')