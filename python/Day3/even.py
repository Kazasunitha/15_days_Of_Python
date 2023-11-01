#Given a list of integers, find all the even numbers and store them in a new list)
n=int(input("Enter the no of elements of lists:"))
l=[]
for i in range(n):
    a=int(input())
    l.append(a)
num=list(filter((lambda x: x%2==0),l))
print(num)

