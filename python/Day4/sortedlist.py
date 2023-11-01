#Create a function that takes a list of strings and returns the list sorted alphabetically"
list1=list(input("Enter the list of strings:").split(" "))
def sortList(l):
      l.sort()
      print(l)
sortList(list1)      