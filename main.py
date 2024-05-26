
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
    split_letters = []
    for i in eval:
        if i.isalpha():
            if i in letters.keys():
                letters[i] += 1
            else:
                letters[i] = 1
    for j in letters.keys():
        split_letters.append({"name":j,"num":letters[j]})
    split_letters.sort(reverse=False, key=sort_on)
    for k in split_letters:
        print(f"The letter '{k["name"]}' occurs {k["num"]} times.")
    print("=== Finished ===")



def sort_on(dict):
    return dict["name"]
    

main()