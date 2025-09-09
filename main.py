import sys
from stats import get_num_of_words, count_of_character, book_stats

def get_book_text(filepath):
    with open(filepath) as book:
        return book.read()
            
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    word_count = get_num_of_words(book_text)
    chars_dict = count_of_character(book_text)
    chars_sorted_list = book_stats(chars_dict)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    
    for char_dict in chars_sorted_list:
        if char_dict["char"].isalpha():
            print(f"{char_dict['char']}: {char_dict['num']}")
    
    print("============= END ===============")


main()