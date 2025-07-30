import sys
from stats import number_of_words
from stats import number_of_characters
from stats import sorted_dictionaries

def get_book_text(filepath):
    with open(filepath) as file:
        return file.read()

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_text = get_book_text(sys.argv[1])
    num_words = number_of_words(book_text)
    char_count = number_of_characters(book_text)
    sorted_char_count = sorted_dictionaries(char_count)
    print("\n============ BOOKBOT ============\n")
    print(f"Analyzing book found at {sys.argv[1]}...\n")
    print("----------- Word Count ----------\n")
    print(f"Found {num_words} total words\n")
    print("--------- Character Count -------\n")
    for item in sorted_char_count:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}\n")

main()
    