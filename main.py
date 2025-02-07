def word_count(string):
    words = string.split()
    return len(words)

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    a = word_count(file_contents)
    print(a) 

if __name__ == "__main__":
    main()