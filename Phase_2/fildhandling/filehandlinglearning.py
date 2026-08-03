'''
in file handling we have 2 types of file 
1-> text files - ex .txt file
2-> Binary files - ex image , pdf
'''

'''
Open function -- modes r-read , w-write, a - append , rb - read binary file , wb - write binary file 

read(), readline(), readlines()
write() and writelines()


'''

# 1 -> Open(filename , mode)
file = open("Data.txt", "w") #-->open the file named Data.txt if exist otherwise create it 

file.write("hellow my name is Aneesh \n")
file.write("I am good")

file.close() # when we open a file we alsways close it aswell after peforming task on the file 


#write lines() - write a hole list  
lines = ["apple\n", "banana\n", "cherry\n"]

file = open("Data.txt" , "w")
file.writelines(lines)

file.close()

# append mode 

file = open("Data.txt" , "a")
file.write("above are fruits name")

file.close()

#reading from a file usin r mode 

f = open("Data.txt", "r")
content = f.read() #- read complete data 
print(content)
print(f.readline()) # - read one line
print(f.readline()) 

print(f.readlines()) # -> read data in the form of list 

for line in f :
    print(line.strip()) #-> remove space from both end of data

f.close() #-> alwasy close file



# with key word ->  file opened using "with" will be accessible within the "with" scope only out side of with file will be closed it remove the closeing file after using 

with open("Data.txt", "r") as file:
    content = file.read()
    print(content)

print(file.read()) # thorw i/o errror as outside of with file is closed 

try:
    with open("Data1.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("file not found")

print("file handling learning")



#  Putting It Together

# save a list of names, then read them back
names = ["Amit", "Neha", "Ravi"]
with open("Data.txt", "w") as f:
    for name in names:
        f.write(name + "\n")


with open("Data.txt", "r") as f:
    for line in f:
        print("Hello,", line.strip())


# Hello, Amit / Hello, Neha / Hello, Ravi
