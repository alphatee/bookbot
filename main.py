from stats import get_book_text, get_word_count, get_character_count

def main():
    book_text = get_book_text("books/frankenstein.txt")

    num_words = get_word_count(book_text)
    num_characters = get_character_count(book_text)

    print(f"Found {num_words} total words")
    print(num_characters)


main()