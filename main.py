def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_counts = get_num_char(text)
    print(f"{num_words} words found in the document")
    for char, count in char_counts.items():
        print(f"'{char}': {count}")


def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_char(text):
    lowered_text = text.lower()
    character_counts = dict()
    for char in lowered_text:
        if char in character_counts:
            character_counts[char] += 1
        else:
            character_counts[char] = 1
    return character_counts

if __name__ == "__main__":
    main()