from stats import number_of_words
from stats import number_of_characters
from stats import sorted_dictionaries

def get_book_text(filepath):
    with open(filepath) as file:
        return file.read()

def main():
    book_text = get_book_text('books/frankenstein.txt')
    num_words = number_of_words(book_text)
    char_count = number_of_characters(book_text)
    sorted_char_count = sorted_dictionaries(char_count)
    print("\n============ BOOKBOT ============\n")
    print(f"Analyzing book found at books/frankenstein.txt...\n")
    print("----------- Word Count ----------\n")
    print(f"Found {num_words} total words\n")
    print("--------- Character Count -------\n")
    for item in sorted_char_count:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}\n")

main()
    