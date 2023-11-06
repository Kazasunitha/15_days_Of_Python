#Implement a function that takes a list of strings and returns a set of unique characters present in all strings
l1=["hello","world","geetha","Jesus"]
def unique(list1):
    for x in list1:
        s=set()
        for i in x:
            s.add(i)
        print(s) 
unique(l1)           