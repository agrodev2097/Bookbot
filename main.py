# main.py
import sys
from stats import get_num_words, char_counts, sort_counts

def main():
    # 1) Проверяем аргументы
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    # 2) Берём путь ко входному файлу
    path = sys.argv[1]

    # 3) Читаем текст книги
    with open(path, encoding="utf-8") as f:
        text = f.read()

    # 4) Выводим общее число слов
    num_words = get_num_words(text)
    print(f"Found {num_words} total words")

    # 5) Выводим частоты только букв, по убыванию
    for item in sort_counts(char_counts(text)):
        ch = item["char"]
        if ch.isalpha():
            print(f"{ch}: {item['num']}")

if __name__ == "__main__":
    main()
