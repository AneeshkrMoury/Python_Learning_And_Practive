'''
practice problem -> 1
1. Build the CountUpTo class with __iter__ and __next__ so for for n in CountUpTo(5) prints 1 to 5. Raise 
StopIteration at the end.
'''
class CountupTo:
    def __init__(self, limit):
        self.limit = limit
        self.current = 1

    def __iter__(self):
        return self
    def __next__(self):
        if self.current > self.limit:
            raise StopIteration
        value = self.current
        self.current = self.current + 1
        return value

obj = CountupTo(10)
for i in obj:
    print(i)


'''
practice Problem 2->
build a custom countdown iterator that counts from n down to 1, then prints "Liftoff!" after the loop.
'''
class CountDown:
    def __init__(self, count):
        self.count = count
    def __iter__(self):
        return self
    def __next__(self):
            if self.count >= 1:
                value = self.count
                self.count = self.count - 1
                return value
            else:
                print("Liftoff!")
                raise StopIteration

obj = CountDown(5)
for i in obj:
    print(i)

'''
Practice Problem -> 3
B1. Write an EvenNumbers iterator that yields the first n even numbers (2, 4, 6, ...) using __iter__ / 
__next__
'''
class EvenNumbers:
    def __init__(self, stop_point):
        self.stop_point = stop_point
        self.current = 2

    def __iter__(self):
        return self
    def __next__(self):
        if self.stop_point < 1:
            raise StopIteration
        value = self.current
        self.current += 2
        self.stop_point -= 1
        return value
          
obj = EvenNumbers(25)
for i in obj:
    print(i)


'''
practice problem -> 4
B2. Build a Repeat iterator that returns the same value n times, then stops.
'''
class Repeat:
    def __init__(self, value, n):
        self.value = value
        self.n = n

    def __iter__(self):
        return self
    def __next__(self):
        if self.n < 1:
            raise StopIteration
        self.n = self.n - 1
        return self.value
    
obj = Repeat("aneesh", 5)
for i in obj:
    print(i)

'''
Practice Problem -> 5
Make a countupto() and pass it to a list Confirm you get the full list — then call list() again and explain the explain the empty result 
'''
class CountupTo2:
    def __init__(self, limit):
        self.limit = limit
        self.current = 1

    def __iter__(self):
        return self
    def __next__(self):
        if self.current > self.limit:
            raise StopIteration
        value = self.current
        self.current = self.current + 1
        return value

obj = CountupTo2(5)
print(list(obj)) # iteraor pointer of obj object start from 1 --> return 1 --> move to 2 --> return 2 ------ similarly till 5 --> return 5 --> now pointer at 6 and > self limit thus raise stop iteration
print(list(obj)) # we call same object so iterator starts from 6 from last point of pointer as it is > self .limit raise stop iteration and return empty list 

'''
Practice Problem -> 6
M1. Write a StepRange(start, stop, step) iterator that mimics range with a custom step. Handle the stop condition correctly.
'''

class StepRange:
    def __init__(self, start, stop, step):
        self.start = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.start >= self.stop:
            print("got the stop")
            raise StopIteration

        value = self.start
        self.start = self.start + self.step
        return value

# handle both positive and negative steps 
class StepRange: 
    def __init__(self, start, stop, step):
        self.start = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.step > 0:
            if self.start >= self.stop:
                raise StopIteration

        elif self.step < 0:
            if self.start <= self.stop:
                raise StopIteration
        else:
            print("invalid step")
            raise StopIteration

        value = self.start
        self.start += self.step
        return value

obj = StepRange(1,10,2)
for i in obj:
    print(i)

'''
Practice Problem -> 7
M2. Build a Fibonacci(n) iterator that produces the first n Fibonacci numbers via __next__ .
'''
# fibonacci number is a sequence that starts from 0 and 1 and next number is the of previous 2 numbers 
# 0 , 1, 1, 2, 3, 5 , 8, 13, 21 so on

class Fibonacci:
    def __init__(self, stop_point):
        self.stop_point = stop_point
        self.a = 0
        self.b = 1
        
    def __iter__(self):
        return self
    def __next__(self):
        if self.stop_point < 1:
            raise StopIteration

        feb = self.a # saving value of a 
        self.a, self.b = self.b, self.a + self.b # updating value of a and b to move ahead in series
        self.stop_point -= 1
        return feb # returning value of feb

obj = Fibonacci(15)
print(list(obj))

'''
Practice Problem -> 8
M3. Make a Cycle iterator over a list that keeps looping the items forever. Test it by pulling 7 values with next() from a 3-item list.
'''
l= ["A", "B", "C"] # we have to pull these 3 items 7 time so i guess we have to play with the stoping point of our next it should not stop normally when reach to end point should be reseted to starting point again 

class Cycle:
    def __init__(self, items):
        self.items = items
        self.starting = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.starting >= len(self.items):
            self.starting = 0
        v = self.items[self.starting]
        self.starting += 1
        return v

obj = Cycle(l)
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
        

'''
Practice Problem -> 9
I1. What two methods must a class define to be an iterator, and what is each responsible for?

Ans -> a class must define iter and next dunder method __iter__ , __next__, __iter__() is responsible for returning an iterator. and Returning the next value and raising StopIteration when there are no more values.
'''

'''
Practice Problem -> 10
I2. Why does a simple custom iterator that returns self from __iter__ only work once, while a list can be looped

Ans -> not sure about it but i think it because it keep its pointer value and when return update and maintain each time will like to understand from u more 
'''

'''
Practice Problem -> 11
I3. How does raising StopIteration inside __next__ end a for loop? Who catches it?

Ans -> i think it being catched by the loop to tell that now there is nothing stop and so far i was using cosidering its a builtin function that is used to tell the loop stop we are above the given limit could u explain it more 
'''
