from stats import get_book_text, get_word_count

def main():
    book_text = get_book_text("books/frankenstein.txt")
    num_words = get_word_count(book_text)
    print(f"Found {num_words} total words")


main()