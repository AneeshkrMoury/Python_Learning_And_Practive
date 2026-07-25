#Dictionary
#dict key can only have hasible value hasible value are int, string, tuple boolean 
#unhashible value  - list , sets 
d1 ={
    "Name":"Aneesh",
    "age":16,
    "marks":[25,30,55],
    "isGood":True,
    "d2":{
        "Name":'Rahul',
        "age": 34
    }
 }
print(d["Nmae"])
print(d[(5,7)])

#dict time complexity is O(n) used to find anything just by one go

# accessing dictionarie

print(d1["d2"])
print(d1.get("Name"))

newd=d1["d2"]
print(newd["Name"])

d3 = dict(name = "Neha", city="Fatehpur",)
print(d3["name"])
list(), tuple(), set(), dict() are constrator 

pairs = dict([("a", 1), ("b", 2),(True, 'I am true')]) # when we give lsit inside a dic constractior and lsit have tuple with 2 values then dict conside 1st element of tuple as key and second element of tuple as value of key 
# print(pairs)


# CRUD  -> Create , Read , Update, Delete
# Action  |  How                       | Example
# Read    |  d[key] or d.get(key)      | d["name"]
# Add     |  d[new_key] = value        | d["email"] = "..."
# Update  |  d[key] = new_value        | d["age"] = 22
# Delete  |  del d[key] or d.pop(key)  | del d["gpa"]


d2 ={
    "Name":"Aneesh",
    "age":16,
    "marks":[25,30,55],
    2:"Hello"
}
d2["average"] = 332.4
print(d2)
d2["Name"]  = "Anni"
print(d2)
del d2[2]
print(d2)
deleted  = d2.pop("marks")#pop is method that delete and return deleted value
print(deleted)

print(d2.get("average"))

# keys return all key of dict and values return value of key in dect 
print(d2.keys())
print(d2.values())

for ele in d2.values():
    print(ele)

print(d2.items())

for k,e in d1.items():
    print(f"{k} : {e}")

l1 = ["python", "javascript", "java", "rust"]
l = {ele : len(ele) for ele in l1}
print(l)

from collections import defaultdict

count = defaultdict(int)

count["apple"] = count["apple"]+1
count["banana"] = count["banana"]+1
count["apple"] = count["apple"]+1

print(count) 
