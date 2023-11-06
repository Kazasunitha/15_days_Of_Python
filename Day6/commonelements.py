#Create a program that finds the common elements between two lists and stores them in a new list$
l1=[1,2,3,4,5,6]
l2=[6,7,8,9,10]
common=[x for x in l1 if x in l2]
print(common)