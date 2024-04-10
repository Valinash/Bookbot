def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_chars = get_num_chars(text)
    sorted_chars = sort_chars(num_chars)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document\n")
    for d in sorted_chars:
        print(f"The '{d["char"]}' character was found {d["num"]} times")
    print("--- End Report ---")    
    

def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_num_chars(text):
    char_dict = {}
    words = text.split()
    for word in words:
        for char in word.lower():
            if char not in char_dict:
                char_dict[char] = 1
            else:
                char_dict[char] += 1
    return char_dict


def sort_on(dict):
    return dict["num"]


"""def sort_chars(char_dict):
    char_list = []
    for key in char_dict:
        if key.isalpha():
            char_list.append({"char": key, "num": char_dict[key]})
    char_list.sort(reverse=True, key=sort_on)
    return char_list"""


# same as above using list comprehension
def sort_chars(char_dict):
    char_list = [{"char": key, "num": char_dict[key]} for key in char_dict if key.isalpha()]
    char_list.sort(reverse=True, key=sort_on)
    return char_list

main()