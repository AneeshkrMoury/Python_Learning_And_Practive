from collections import namedtuple


#namedtuple -> in named tuple we give name to each value instead on idnex number 
# 1->> import namedtuple factory function 
# 2->> create class a blueprint of tuple 
Employee = namedtuple('Employee', ['id', 'Name', 'salary'])
# thing it like employee name forma is created and have these values id , name , salary 

# 3 -->> create object of class

s1 = Employee(1,"Aneesh", 20200) 

# 4 -->> access way for named tuple

print(s1.id,s1.Name,s1.salary)
print(s1[0])

# coverting lsit into namedtuple usink ._make() method 
l1 = [45,"Ankita", 340520]
s2 = Employee._make(l1)

print(s2.id, s2.Name, s2.salary)

#coverting named tupple object into dict using ._asdict
d1 = s2._asdict()
print(d1)

# to repalce any specific element in namedtuple  ._repalce
s1 = Employee(1,"Aneesh", 20200) 

new_s1 = s1._replace(salary=400000)
print(s1)
print(new_s1)

# to find field of any named tuple ->>  ._fields
print(s1._fields)
