#Create a program that takes a year as input and checks if it is a leap year or not
def isleapyear(year):
    if(year%400==0):
        print("Leap Year")
    elif(year%4==0 and year%100!=0)  :
        print("Leap Year")  
    else:
        print("Not a leap year")  
y=int(input("enter a year:"))
isleapyear(y)          
 

