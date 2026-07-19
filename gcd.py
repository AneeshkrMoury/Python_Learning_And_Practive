num_one = int(input("enter first number : "))
num_two = int(input("enter second number : "))


a = abs(num_one)
b = abs(num_two)

#gcd = None
if num_one == 0 or num_two == 0:
    print("Both numbers must be non-zero")
else:
    while b:
        a, b = b, a % b

    print(f"GCD of enterd numer {num_one} and {num_two} = {a}")

    







