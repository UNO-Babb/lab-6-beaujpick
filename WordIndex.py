#WordIndex.py
#Name:Beau Pick
#Date:10/5/25
#Assignment:

def build_word_index(filename):
    """Create a dictionary of words with lists of line numbers where they appear."""
    file = open(filename, 'r', encoding='utf-8')
    lines = file.readlines()
    file.close()

    words = {}  

    for line_num, line in enumerate(lines, start=1): 
        for word in line.strip().split():
            word = word.lower().strip('.,!?;:"()[]{}') 
            if word: 
                if word not in words:
                    words[word] = [line_num]
                elif line_num not in words[word]:
                    words[word].append(line_num)

    
    for word in sorted(words):
        print(f"{word}: {words[word]}")

def main():
    filename = input("Enter a File Name: ")
    build_word_index(filename)

if __name__ == "__main__":
    main()
