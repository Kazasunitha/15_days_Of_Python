#Write a program that calculates the factorial of a given number) 
def factorail(num):
    if(num==0):
        fact=1
    else:
        fact=1
        for i in range(1,num+1):
            fact=fact*i 
    return fact
n=int(input("Enter an number:"))
print(factorail(n))
