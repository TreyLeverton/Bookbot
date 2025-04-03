from stats import count_words
from stats import char_count
from stats import sort_chars

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    path = "books/frankenstein.txt"
    text = get_book_text(path)
    num_words = count_words(text)
    chars_dict = char_count(text)
    sorted_list = sort_chars(chars_dict)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    
    for item in sorted_list:
        char = item["char"]
        if char.isalpha():
            print(f"{char}: {item['count']}")
    
    print("============= END ===============")

if __name__ == "__main__":
    main()