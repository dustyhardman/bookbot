import sys
from stats import get_num_words

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)


def main():
    path = sys.argv[1]
    text = get_book_text(path)
    num_words = get_num_words(text)
    char_counts = get_num_char(text)
    sorted_char_counts = sort_char_counts(char_counts)

    # Print the formatted report
    print(f"--- Begin report of {path} ---")
    print(f"{num_words} words found in the document\n")

    for char, count in sorted_char_counts:
        print(f"The '{char}' character was found {count} times")

    print("--- End report ---")


def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_num_char(text):
    lowered_text = text.lower()
    character_counts = dict()
    for char in lowered_text:
        if char.isalpha():
            if char in character_counts:
                character_counts[char] += 1
            else:
                character_counts[char] = 1
    return character_counts


def sort_char_counts(character_counts):
    return sorted(character_counts.items(), key=lambda x: x[1], reverse=True)


if __name__ == "__main__":
    main()
