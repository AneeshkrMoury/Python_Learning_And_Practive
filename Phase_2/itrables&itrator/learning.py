nums = [10,20,30,40,50]
# for i in nums:   # how it works -> at backgrount oython create a iterator named x 
#     print(i)


# somethink like this happens in background when we do a loop
it = iter(nums)
while True: 
    try:
        x = next(it)
    except StopIteration:
        break
    print(x)

'''
in this we get iterables and terators
'''

# itrables 
nums = [10,20,30,40,50]  #on item on which loops work are itrables 
# print(nums)

#itrator

it = iter(nums)# covert an item into itrators 
print(it) # return memory address we can not access it normally to access it we use next keyword
print(next(it)) # return 1st item
print(next(it)) # return 2nd item
print(next(it)) # return 3rd item
print(next(it))
print(next(it))


#iterables  have a dunder method -> __iter__
# iterator have 2 dunder method -> __iter__, __next__
