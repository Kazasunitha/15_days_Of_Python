#Write a program to check if a number is prime
n=int(input("enter a number:"))
def checkPrime(num):
    count=0
    for i in range(1,num+1):
        if(num%i==0):
            count+=1
    print("Prime" if(count==2) else " Not prime") 
checkPrime(n)     