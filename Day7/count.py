#Write a Python program that counts the number of occurrences of each character in a given string using a dictionar
string=input("enter a string:")
def count_chars(string):
    dict1={}
    for char in string:
        if char in dict1:
            dict1[char]+=1
        else:
            dict1[char]=1
    return dict1
print(count_chars(string))            