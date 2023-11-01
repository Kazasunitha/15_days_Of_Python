#Given a list of words, count the number of words with more than five characters)
l=["pscmr","HelloWorld!","Number","Friend","Bahubali"]
def count(list1):
    wordCount=0
    for word in list1:
        c=0
        for ch in word:
            c+=1
        if(c>5):
            wordCount+=1
    return wordCount
print(count(l))        



