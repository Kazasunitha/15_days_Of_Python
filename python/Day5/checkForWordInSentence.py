#Implement a program that takes a sentence and a word as input and checks if the word is present in the sentence
word=input("enter a word:")
sentence=list(input("enter a sentence:").split(" "))
if word in sentence:
    print("yes")
else:
    print("No")    