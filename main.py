def read_book(book_path):
    with open(book_path) as f:
        file_contents = f.read()
    return file_contents

def count_words(text):
    words = text.split()
    return len(words)

def count_chars(text):
    lower_text = text.lower()
    uchars = sorted(set(lower_text))
    char_counts = {}
    for uc in uchars:
        char_counts[uc] = 0
    for c in lower_text:
        char_counts[c] += 1
    return char_counts

def gradeup(object): # get indices for sorting up
    l = list(object)
    return sorted(range(len(l)), key=lambda k: l[k])

def print_report(wc, cc):
    print(f"{wc} words found in the document\n")
    index = gradeup(cc.values())
    for i in index[::-1]:
        key = list(cc.keys())[i]
        if key.isalpha():
            print(f"The \'{key}\' character was found {cc[key]} times")

def main():
    book_path = "books/frankenstein.txt"
    book_contents = read_book(book_path)
    # print(book_contents)
    wc = count_words(book_contents)
    # print(wc)
    cc = count_chars(book_contents)
    # print(cc)
    print_report(wc, cc)

main()