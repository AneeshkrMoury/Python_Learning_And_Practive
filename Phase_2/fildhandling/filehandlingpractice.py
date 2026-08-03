#Practice problem -1
'''Write & Read Back
Using with , write three lines of text to Data.txt then open it again and print the whole file '''

with open("Data.txt", "w") as file:
    lines  = ["My name is Aneesh", "I am a student", "I love python"]
    for line in lines:
        file.write(line + "\n")


with open("Data.txt", "r") as file:
    for line in file:
        print(line) # with this output was print a empty line as well because we used \n
        print(line.split()) # outlooks line this  ['My', 'name', 'is', 'Aneesh']
        print(line.split("\n")) # output look like this ['I love python', '']
        print(line.removesuffix("\n") )  # works perfectly it remove empty line and print My name is Aneesh similary other two
        print(line.strip()) # it also give similer result to remove suffix one it better and easy to remeber as well
    

#practice problem 2 ->
# Safe File Reader
# Ask the user for a filename and print its contents. Use try/except so a missing file prints "File not found" instead of crashing.

try: 
    file_n = input("enter file name : ")
    with open(file_n, "r") as f:
        for line in f:
            print(line)
except FileNotFoundError:
    print("file not found")


#practice question - 3
'''Save a Quote
Write your favourite quote to a file quote.txt using with and write mode. Then read it back and print it.'''

with open("Data.txt", "w") as f:
    f.write("we are not compititing with others just focus on becomming better then you were yesterday")

with open("Data.txt", "r") as f:
    for line in f:
        print(line)


#practice question - 4
'''Append a Log log.txt in append mode and add a new line each time the program runs. Run it 3 times and confirm all three lines are there (nothing erased).'''

with open("log.txt", "a") as f:
    f.write("apeending new txt\n")

reading to confirm append worked 

with open("log.txt", "r") as f:
    for l in f:
        print(l) # apeending new txtapeending new txtapeending new txt


#practice question -5
# Count the Lines
# Read a text file and print how many lines it contains.

with open("Data.txt", "r") as f: 

    #build in method
    length = len(f.readlines())
    print(length)

     count = 0
    for l in f:    #
        count = count + 1 #custome method 
    print(count)
   

# Practice Problem - 6
# Word Counter Read a text file and count the total number of words in it. (Split each line and addup.)

with open("Data.txt", "r") as f:
    word_count = 0
    for line in f:
        word_count = word_count + len(line.split())

    print(word_count)


#practice problem - 7
# Copy a File
# Read all content from source.txt and write it into copy.txt use two ith blocks (or one nested). Handle the case where the source is missing.

try: 
    with open("Data.txt", "r") as f1:
        for l in f1:
            with open("copy.txt", "a")as f2:  # here first i tried w but it does not work so i moved to a as append add just after what is written already in file without removing any thing 
                f2.write(l)
except FileNotFoundError:
    print("data file not found")

with open("copy.txt", "r") as f2:
    for l in f2:
        print(l.strip())  

'''output is exact same as data.txt we are not compititing with others
just focus on becomming better then you were yesterday'''


#practice question - 8
'''Simple Notes App
Write a mini program: ask the user to type notes line by line until they type "quit" . Save all notes to notes.txt , then read the file back and print every note numbered '''

with open("notes.txt", "a") as n:
    while True:
        note = input("enter notes : ")
        if note == "quit":
            break

        n.write(note + "\n")

with open("notes.txt", "r") as n:
    for seq , note in enumerate(n):
        print(f"{seq+1} --> {note.strip()}")


#practice question - 9:
'''Most Common Word Read a text file, and find the word that appears most often. Use counter from #14. Print the word and its count'''

from collections import Counter
with open("notes.txt", "r") as notes:
    words = notes.read()
    count = Counter(words.split())
    word_count = 0
    word = None
    for w,c in count.items():
        if word_count < c:
            word_count = c
            word = w

    print(f" most appeard word -> {word} \n most appeard word count ->  {word_count}")


#practice problem 10
'''Remove Duplicate Lines
Read a file that may have duplicate lines. Write a new file containing only the unique lines, keeping their first order of appearance'''

with open("notes.txt", "r") as note, open("uniqe.txt", "a") as unique:
    line = []
    for i in note:
        if i not in line:
            line.append(i)

    for j in line:
        unique.write(j)   


# Predict the Output
# You run this twice. What's in 
# data.txt after the SECOND run, and why?
with open("data.txt", "w") as f:
    f.write("hello\n")
with open("data.txt", "a") as f:
    f.write("world\n")

#output -> on first run -> first with open file in write mode ---> write "hello" and shift to new line --> after this move to 2nd with --> it open file in append mode --> add the world in new line ===================first run over =======================
#on second run --> first with open file in wirte mode --> as its in write mode ---->it will clear all data presetn ----> then write hello on first line -->move to sencont line ----> now 2nd with runs --->it open file in append mode ---> add world in second line ==========second run over aswell==========================
#thus final output will be 
'''
hello
world
'''

