#Write a function to remove all duplicate characters from a given string
def removeduplicate(word):
    unique=""
    for i in word:
        if i not in unique:
            unique+=i
    print(unique)    
string=input("enter a string:")
removeduplicate(string)       
    