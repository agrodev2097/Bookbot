def get_num_words(file_contents):
    return len(file_contents.split())

def char_counts(text: str) -> dict[str, int]:
    """
    Возвращает словарь частот символов (включая пробелы и знаки).
    Подсчёт регистронезависимый.
    """
    counts: dict[str, int] = {}
    for ch in text.lower():
        counts[ch] = counts.get(ch, 0) + 1
    return counts

def sort_counts(counts: dict[str, int]) -> list[dict[str,int]]:
    items = [{"char": ch, "num": n} for ch, n in counts.items()]
    items.sort(key=lambda d: d["num"], reverse=True)
    return items