#Create a function to reverse a given string
word=input("enter the string:")
def reverseOfString(word):
    reverse=word[::-1]
    print("reverse word of ",word," is ",reverse)
reverseOfString(word)    