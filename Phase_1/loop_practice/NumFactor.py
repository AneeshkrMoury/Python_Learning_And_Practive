num = int(input("ener a number to chekc its factors : "))

print(f"Factors of entered {num} number are : ", end="")

for i in range(1,num):
    if num % i == 0:
        print(i, end=", ")
      
