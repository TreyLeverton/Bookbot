def count_words(text):
    words = text.split()
    return len(words)

def char_count(text):
    chars = {}
    lowercase = text.lower()
    for char in lowercase:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    return chars
    
def sort_chars(char_dict):
    char_list = []
    for char, count in char_dict.items():
        char_list.append({"char": char, "count": count})

    def sort_on(dict):
        return dict["count"]

    char_list.sort(reverse=True, key=sort_on)
    
    return char_list

