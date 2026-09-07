'''
S1. Write a closure multiplier(factor) that returns a function multiplying its input by factor . Build double and
triple from it.
'''
def multiplier(factor):
    def multiplying(n):#it sould take number be like take 2 if we want to double our number or 3 if need triple 
        return n*factor

    return multiplying

lets try to call it 
onj = multiplier(5) # now here onj hold multiplying function so when we call it we need to pass a value 

print(onj(2)) #double 
print(onj(3)) # triple
