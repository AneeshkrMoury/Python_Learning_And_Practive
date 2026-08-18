# passward generator 

import random 
import string

def Generate_passward(len_passward):
    charcter = string.ascii_letters + string.digits + string.punctuation
    passward = ""
    
    if len_passward <= 0:
        print("Enter a positve size in digits....")
        print()
    else:
        print("======== Generating Passward =========")
        print()
        for _ in range(len_passward):
            passward = passward + random.choice(charcter)
        return passward

try:
    len_pswd = int(input("Enter Passward Size:"))
    print(f"Passward : {Generate_passward(len_pswd)}")
except ValueError:
    print("Enter a valid size in digits......")
