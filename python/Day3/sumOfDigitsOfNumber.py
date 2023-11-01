#Calculate the sum of digits of a given number.

n=input("Enter a number:")

def sum(num):
    s=0
    for i in num:
        s+=int(i)
    return s
print(sum(n))    


