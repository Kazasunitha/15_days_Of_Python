#Implement a program that prints the multiplication table of a given number
def table(n):
    for i in range(1,11):
        print(n," * ",i," = ",n*i)
num=int(input("enter a number:")) 
table(num)       
