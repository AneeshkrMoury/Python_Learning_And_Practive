#finds the most frequently appearing number in the list.
numbers = [4, 7, 2, 7, 9, 4, 7, 3, 2, 9, 7]

# we will try to use dict and store the number as key and the apperance as value ;
def frequency(data):
    appearnce = 0
    number = None
    feq_dict = {}
    for i in data:
        if i not in feq_dict:
            feq_dict[i] = 1
        else:
            feq_dict[i] = feq_dict[i] + 1
        if number is None or appearnce < feq_dict[i]:
            number = i
            appearnce = feq_dict[i]
    return f"Most appeard Number -> {number}\nFrequency of apperance -> {appearnce}"
print(frequency(numbers))



