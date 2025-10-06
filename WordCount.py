#WordCount.py
#Name:Beau Pick10/5/25
#Date:
#Assignment:

def wc(filename):
    """Count lines, words, and characters in a file."""
    file = open(filename, 'r', encoding='utf-8')
    lines = file.readlines()
    file.close()
    
    line_count = len(lines)
    word_count = sum(len(line.split()) for line in lines)
    char_count = sum(len(line) for line in lines)

    print("Lines:", line_count)
    print("Words:", word_count)
    print("Characters:", char_count)

def main():
    filename = input("Enter a File Name: ")
    wc(filename)

if __name__ == "__main__":
    main()


