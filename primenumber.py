a = int(input("enter a number  : "))

i = 2

if a <= 1 :
    print(f"{a} is not a Prime Number")
else:
    while i*i <= a:

        if a%i == 0:
            print(f"{a} is not a Prime Number")
            break
    
        i = i+1
    else:
        print(f"{a} is a Prime Number")
