from stats import character_count
from stats import count_words
import sys


"""def main(book_file):
    num_words = count_words(book_file)
    print(f"{num_words} words found in the document")"""

def main(book_file):
    print("============ BOOKBOT ============")
    print("Analyzing book found at "+ book_file + "...")
    print("----------- Word Count ----------")
    print(f"Found" , count_words(book_file) , "total words")
    print("--------- Character Count -------")
    for entry in character_count(book_file):
        print(f"{entry['char']}: {entry['num']}")
    print("============= END ===============")

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
book_file = sys.argv[1]

main(book_file)
