def get_book_text(path_to_file:str) -> str:
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def get_word_count(file_contents:str) -> int:
    word_count = file_contents.split()
    return len(word_count)

def main():
    book_text = get_book_text("books/frankenstein.txt")
    num_words = get_word_count(book_text)
    print(f"Found {num_words} total words")


main()