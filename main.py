
def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        words = file_contents.split()
        count = 0
        for word in words:
            count += 1
        print("--- Analysing book ---")
        print(count," words found.")
        countLeters(file_contents)



def countLeters(book):
    letters = {}
    eval = book.lower()
    for i in eval:
        if i in letters.keys():
            letters[i] += 1
        else:
            letters[i] = 1
    for j in letters.keys():
        print(f"{j} used {letters[j]} times")
    print("=== Finished ===")
    



main()