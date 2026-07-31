# boolean -> it is a data type that stores 2 values True and False ; its foundation of decision making in programming , every if statement , loop condition and logical decision ultimatily evalutates to eother True or False 

a = True
b = False
print(type(a))
print(type(b))


# compresion Operators -> those operator used to compare 2 or more values to return either true r=or false == != > < >= <= 
x = 9
x==7 # relational expersion  or coparsion expersion also said boolean expersion 
print(x > 7) #  relational expersion  or coparsion expersion also said boolean expersion 
print(x==7)

'''
Truth Tables --> includes AND OR  both work on boolean values
AND operator
True and True   --> True
True and False  --> False
False and True  --> False
False and False --> False

OR operator
True and True   --> True
True and False  --> True
False and True  --> True
False and False --> False
'''

print(True and False )
print(True and True )

print(True or False )
print(True or True )

a=True
b=False
c=True

print(a and not b and  c)
print(not a or b or not c)

age = 24
c_s = 40


print (age > 18 and c_s>40)
print (age > 18 or c_s>40) # as age > 18 return true and c_s > 40 return false thus AND , OR works in expersion compresion aswell

#falsiy vlaue 
#None , Empty 
