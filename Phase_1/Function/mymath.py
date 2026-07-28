def  add(a,b): #addition function
    return a + b

def is_prime(n):  #prime checker function 

    if n <= 1 :
        return False
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i = i+1
    else:
        return True
