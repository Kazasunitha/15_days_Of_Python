#Create a function that takes a list of strings and returns the list sorted by the length of the strings$
def sortBYLen(list1):
    list1.sort(key=len)
    print(list1)
l=["Mango","Kiwi","Dragon","Apple"]  
sortBYLen(l)  