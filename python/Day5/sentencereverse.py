#Create a function that takes a sentence as input and returns the sentence in reverse order
def reverse(sen):
    l=list(sen.split(" "))
    rev=l[::-1]
    revsen=""
    for i in rev:
        revsen+=i+" "
    return revsen    

sentence=input("enter a sentence:")
print(reverse(sentence))
