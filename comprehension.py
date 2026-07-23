# list comprehension
l1 =[i*i for i in range(1,10) if i%2==0]
print(l1)

# set comprehension

s1 = {i*i for i in range(1,10)}
print(s1)

names = ["ravi", "Anil", "sara", "enha","ram"]

len_set =  {len(ele) for ele in names if len(ele)%2==0}
print(len_set)

words = ["hi", "python", "set"]
lenght = {w:len(w) for w in words}
print(lenght)
print(type(lenght))

nums = [1,2,3,4,5,6]
squar_num = {n: n*n for n in nums if n%2==0}
print(squar_num)
