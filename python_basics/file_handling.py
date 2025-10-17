with open("example.txt", "w") as f:
    f.write("Hello World\n")
with open("example.txt", "r") as f:
    content = f.read()
    print(content)
with open("example.txt", "a") as f:
    f.write("This is appended text.\n")
with open("example.txt", "r+") as f:
    content = f.read()
    print("Before:", content)
    f.write(" Adding new text.")

'''
Hello World

Before: Hello World
This is appended text.
'''

with open("example.txt", "a") as f:
     f.write("Hello \n World \n Python")
with open("example.txt", "r") as f:
    content = f.read()
    print(content)



with open("example.txt", "r") as f:
    line1 = f.readline()
    line2 = f.readline()
    line3 = f.readline()
    print("Line 1:", line1)
    print("Line 2:", line2)
    print("Line 3:", line3)
with open("example.txt", "r") as f:
    lines = f.readlines()
    print(lines)

def count_words_and_lines(filename):
    try:
        with open(filename,"r") as file:
            lines = file.readlines()
            line_count = len(lines)
            word_count = sum(len(line.split())for line in lines)
            
            print(f"Number of lines is {line_count}")
            print(f"Number of words is {word_count}")
    except FileNotFoundError:
        print(f"{filename} not found")



def write_item_to_file(filename, items):
    with open(filename, "w") as file:
        for item in items:
            file.write(item + "\n")
write_item_to_file("shopping.txt", ["Apples", "Bananas", "Milk"])
def read_items_from_file(filename):
    try:
        with open(filename, "r") as file:
            items = file.readlines()
            print("Items in the file:")
            for item in items:
                print(item.strip())
    except FileNotFoundError:
        print(f"File {filename} not found!")
        
read_items_from_file("shopping.txt")

def copy_file(src, dest):
    try:
        with open(src, "r") as f_src:       # open source file in read mode
            content = f_src.read()          # read everything
        with open(dest, "w") as f_dest:     # open destination file in write mode
            f_dest.write(content)           # write contents into new file
        print(f"Copied contents from {src} to {dest}")
    except FileNotFoundError:
        print(f"Source file {src} not found.")
# Example
copy_file("shopping.txt", "shopping2.txt")



def count_word(filename, word):
    try:
        with open(filename, "r") as f:
            text = f.read().lower()            # convert everything to lowercase
            word = word.lower()
            count = text.split().count(word)   # split text into words and count
            print(f"The word '{word}' occurs {count} times in {filename}")
    except FileNotFoundError:
        print(f"File {filename} not found.")
# Example
count_word("shopping.txt", "apples")

import datetime
def log_message(filename, message):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(filename, "a") as f:           # append mode, don't erase file
        f.write(f"[{timestamp}] {message}\n")
    print("Message logged!")
# Example
log_message("log.txt", "Program started")
log_message("log.txt", "User logged in")

'''
Hello World
This is appended text.
 Adding new text.Hello
 World
 Python
Line 1: Hello World

Line 2: This is appended text.

Line 3:  Adding new text.Hello

['Hello World\n', 'This is appended text.\n', ' Adding new text.Hello \n', ' World \n', ' Python']
Items in the file:
Apples
Bananas
Milk
Copied contents from shopping.txt to shopping2.txt
The word 'apples' occurs 1 times in shopping.txt
Message logged!
Message logged!
'''