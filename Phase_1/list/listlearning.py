a = [1, 2, 3]
b = a
b.append(4)
print(a,b)

#list =  is ordered and mutable collection that can hold items of any type, ordered , allow dublicate 

# example -> 

a =["Aneesh", 32, True, 87.5, 67]
accessing list element 
print(a[0])
print(a[3])
print(a[-5])

#finding len of list
print(len(a))

#looping through list 

for i in range(0,len(a)):
    print(a[i])


i = 0
while i != len(a):
     print(a[i])
     i+=1

y = list(("Aneesh", 32, True, 87.5, 67))
print(y)

letters = list("Aneesh")
print(letters)

#slicing 
list[start:stop:step]

mini_list = a[::2]
print(mini_list)

#revering a list 
reverse_a = a[::-1]
print(reverse_a)


# modifiying list 
a =["Aneesh", 32, True, 87.5, 67]
# 1 append 
a.append("student hai")
# .insert(position, value to insert)
a.insert(1, 86)
print(a)
# .remove(element to remove )
a.remove("Aneesh")
#  pop() remove and return last element 
print(a.pop())
print(a)
# replacing element 
a[2] = 12
print(a)

#nested list 
l1 = [12, [True, False, 34,[58,54,85]], 45]
print(l1[1:2])
print(l1[1][3][0])

point = [10, 20, 30, 40, 50]
x, y, *z = point
print(x, y, z)
