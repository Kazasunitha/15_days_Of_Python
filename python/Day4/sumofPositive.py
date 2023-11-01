#Given a list of numbers, create a function to find the sum of all positive numbers"
list1=[1,-1,6,-10,-18,2,24,-9]
list2=[x for x in list1 if x>0]
print(sum(list2))