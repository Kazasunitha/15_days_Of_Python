#Write a program that checks if a given list is sorted in ascending order$
l1=[18,6,1,9,65]
def isSorted(l):
     givenList=l
     sortList=l.sort()
     print("Yes" if(givenList==sortList) else "No")
isSorted(l1)     