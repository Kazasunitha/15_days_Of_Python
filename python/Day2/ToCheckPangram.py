#Write a Python program to check if a given string is a pangram (contains all letters of the alphabet)

def ispangram(str):
    alphabet="abcdefghijklmnopqrstuvwxyz"
    for i in alphabet:
        if i not in str.lower():
            return False
    return True     

var="Hello i am student"            
print(ispangram(var) )             