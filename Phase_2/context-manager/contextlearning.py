f = open("note.txt", "r")
data = f.read()
result = 10/ 0 # due to this file do not close we can use try: and finaaly here but what if someone forget to write file.close() then here comes the concept of clotext manager
f.close()

'''when we use context manage and  come out of its context / intent it automatically get closed'''
with open("note.txt", "r") as f:
    print(f.read())

print("hello")


'''
Many things must be opened and then closed: files, database connections, network sockets, locks. if you open a file and forget to close it, or an error strikes before  close() , the resource stays open and data can be lost
'''

#how it work
'''
A context manager is any object with two special methods: 
protocol. When Python runs a __enter__ and with statement, it follows these exact steps:
'''

#context manager
class Abc:
    def __enter__(self):
        pass
    def __exit__(self):
        pass

# we can write like
with Abc() as f:
    pass

# how with works
'''
Step   What Python does                                      In with open('notes.txt') as f:
1      Evaluates the object after                            open('notes.txt') returns a file object
2      Calls its with __enter__() method                     prepares the file for use
3      Stores what __enter__ returned in the as variables    f = the file objec
4      Runs the indented block                               your reading / writing code 
5      Calls __exit__() — always                             closes the fil

'''

import time

class Timer:
    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc, tb):
        end = time.time()
        print(f"Took: {end -self.start:.2f}s")
        return False

with Timer() as t:
    total = sum(range(10_00_00_000))

print("Total:", total)
