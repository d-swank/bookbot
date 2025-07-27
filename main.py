def get_book_text(filepath):
    with open(filepath) as file:
        return file.read()
  
def main():
    book_text = get_book_text('books/frankenstein.txt')
    print(book_text)

main()
    