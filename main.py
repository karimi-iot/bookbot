def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{count_words(text)} words found in the document\n")
    char_count = count_chars(text)
    for char in char_count:
        print(f"The '{char["name"]}' character was found {char["count"]} times")
    print("--- End report ---")
    



def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    text = text.split()
    return(len(text))

def count_chars(text):
    text = text.lower()
    # chars = "abcdefghijklmnopqrstuvwxyz"
    chars_count = {}
    # for ch in chars:
    #     count = text.count(ch)
    #     chars_count[ch]= count
    
    for char in text:
        if not char.isalpha():
            continue
        if char in chars_count.keys():
            chars_count[char] += 1
        else :
            chars_count[char] = 1 
    chars_count = sorted([{"name": char[0], "count": char[1]} for char in chars_count.items()], reverse=True, key=lambda x: x['count'])
    return chars_count


main()
