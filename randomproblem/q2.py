# calculate the highest frequesnce element  and also count apperance of element 
p = ["a","d","e","f","c","s","a","a","b","d","e","c"]

def Apperance_checker(lst):
    most_appeared = None
    temp = {}
    for i in lst:
        if i not in temp:
            temp[i] = 1
        else:
            temp[i] = temp[i] + 1

        if most_appeared == None:
            most_appeared = i
        else:
            if temp[most_appeared] < temp[i]:
                most_appeared = i

    return f"Most Appeared element = {most_appeared} \nFrequency of Appearance of each item = {temp}"

print(Apperance_checker(p))
