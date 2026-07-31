# x = 5
# if 3 > x > 3 :
#     print("yes")
# else: 
#     print("no") # return  no 

# wap to check number type 

# n = int(input("enter number : "))
# if n > 0:
#     print("positvie number")
# elif n < 0:
#     print("negative number")
# else :
#     print("Number is zero")

#wap to display the even or odd  consider user will not enter o
# n = int(input("enter number : "))
# if n % 2 ==  0:
#     print("even number")
# else:
#     print("odd number")

# #grade calculator 
# def grade_calculator(marks):
#     if marks >= 90:
#         return "A"
#     elif marks >= 80:
#         return "B"
#     elif marks >= 60:
#         return "C"
#     elif marks >= 40:
#         return "Promoted TED"
#     else:
#         return "Fail"


# mark = int(input("enter your marks : "))
# print(grade_calculator(mark))


# WAP to get 3 number input from user and find gratest number also do not use and or operaotor use nested if else also cosider user will enter different numbers

# a = int(input("enter a number : "))
# b = int(input("enter b number : "))
# c = int(input("enter c number : "))

# if a > b :
#     if a > c:
#         print(f"a'{a}' is gratest number ")
# if b > a :
#     if b > c:
#         print(f"b'{b}' is gratest number ")
# if c > b :
#     if c > a:
#         print(f"c '{c}' is gratest number ")

# mark = int(input("enter your marks : "))
# if mark >= 40 and mark <= 100:
#     print("pass")
# else:
#     print("fail")

# print("Pass" if mark >= 40 else "Fail")

 
#match case -> where get matched return or print
letter = input("wnter letter : ")

match letter:
    case "A":
        print(letter, " is vowel")
    case "E":
        print(letter, " is vowel")
    case "I":
        print(letter, " is vowel")
    case "O":
        print(letter, " is vowel")
    case "U":
        print(letter, " is vowel")
    
