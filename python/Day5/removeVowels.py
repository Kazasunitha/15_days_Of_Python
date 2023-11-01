#Given a string, write a function to remove all vowels from it and return the modified string
def remove(str):
    vowels=['a','i','e','o','u']
    string=""
    for x in str:
        if x not in vowels:
            string+=x
    return string
str=input("enter a string:")  
print(remove(str))      