#Given a list of numbers, find the sum and average
l1=input("enter the list of elements:").split(" ")
l1=list(map(lambda x:int(x),l1))
add=sum(l1)
average=add/(len(l1))
print("sum=",add)
print("Average=",average)
