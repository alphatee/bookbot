from collections import Counter

def get_book_text(path_to_file:str) -> str:
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def get_num_words(file_contents:str) -> int:
    word_count = file_contents.split()
    return len(word_count)

def get_chars_dict(file_contents:str) -> dict[str,int]:
    format_data = file_contents.lower()
    return Counter(format_data)

def chars_dict_to_sorted_list(data:dict[str,int]) -> list[dict[str,int]]:
    new_list = []

    # filter input to exclude non alpha characters
    for key, value in data.items():
        if not key.isalpha():
            continue

        # format input as a composite dictionary of two dictionaries
        new_dict = { "char": key, "num": value }
        # add the composite dictionary to the list
        new_list.append(new_dict)

    # sort the new list from greatest to least frequency and sort on the composite dictionary key
    new_list.sort(reverse=True, key=sort_on)
    # return the new list of composite dictionaries
    return new_list

# helper free fuction
def sort_on(data:dict[str,int]) -> int:
    return data["num"]
