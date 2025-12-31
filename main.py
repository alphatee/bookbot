from stats import get_book_text, get_num_words, get_chars_dict, chars_dict_to_sorted_list
import sys

####################################################################

def main():
    ####################################################################
    # Explain how to use program
    ####################################################################
    print("============ MAN PAGE ============")
    print("Usage: python3 main.py <path_to_book>")
    print(''' Path to Book listed below:
    books/frankenstein.txt
    books/mobydick.txt
    books/prideandprejudice.txt
    ''')
    if sys.argv[0] and sys.argv[1] == False:
        sys.exit(1)

    ####################################################################
    # Execute Program
    ####################################################################
    file_name = sys.argv[1]
    book_text = get_book_text(file_name)

    num_words = get_num_words(book_text)
    num_characters = get_chars_dict(book_text)

    # print(f"Found {num_words} total words")
    # print(num_characters)

    ####################################################################
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_name}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    ###
    list_of_dicts = chars_dict_to_sorted_list(num_characters)
    for item in list_of_dicts:
        print(f"{item["char"]}: {item["num"]}")
    ###

    print("============= END ===============")

####################################################################
# Entry Point
####################################################################
main()