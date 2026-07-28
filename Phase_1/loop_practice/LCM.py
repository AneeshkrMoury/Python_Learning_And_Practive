num_one = int(input("enter first number : "))
num_two = int(input("enter second number : "))

greater_num = None

if num_one > num_two:
    greater_num = num_one
else:
    greater_num = num_two

lcm = 1 

if num_one == 0 or num_two == 0:
    print("enter both number less then or greather then  0 ")
else:
    for i in range(2, greater_num + 1):

        while num_one % i == 0 or num_two % i == 0 :
        
            if num_one % i == 0 :
                num_one = num_one // i

            if num_two % i == 0 :
                num_two = num_two // i 

            lcm = lcm * i


    print(lcm)


    







