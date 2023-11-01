#Write a Python program to find the length of the longest word in a sentence
sen=list(input("enter a sentence:").split(" "))
length=max([len(x) for x in sen])
print(length)