#Implement a program that converts a given number of minutes into hours and minutes
min=int(input("enter minutes:"))
def convert(m):
    hours=m//60
    minutes=m%60
    print("The given ",m,"is equal to",hours,"hrs:",minutes,"mins")
convert(min)    