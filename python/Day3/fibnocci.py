#Create a program that generates the Fibonacci sequence up to a given number of terms


n=int(input("enter a number:"))
def fib(num):
    a=0
    b=1
    print(a)
    print(b)
    for i in range(2,num):
            k=a+b
            print(k)
            a,b=b,k
fib(n)        


        
