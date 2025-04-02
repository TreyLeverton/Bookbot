
def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
    
    def main():
        path = "frankenstein.txt"
        text = get_book_text(path)
        print(text)

    if __name__ == "__main__":
        main()