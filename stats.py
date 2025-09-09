def get_num_of_words(book_text):
    split_words = book_text.split()
    return len(split_words)

def count_of_character(book_text):
    character_dict = {}
    for char in book_text:
        lower_case_char = char.lower()
        if lower_case_char in character_dict:
            character_dict[lower_case_char] += 1
        else:
            character_dict[lower_case_char] = 1
    return character_dict

def sort_on(dict_item):
    return dict_item["num"]

def book_stats(chars_dict):
    character_dict_report = []
    for char, num in chars_dict.items():
        character_dict_report.append({"char": char, "num": num})
    return sorted(character_dict_report, key=sort_on, reverse=True)