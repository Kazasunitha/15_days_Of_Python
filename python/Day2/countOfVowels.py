#Create a function to count the number of vowels in a given string
aString=input("enter a string:")
def vowelsCount(sen):
    vow=['a','e','i','o','u']
    count=0
    for i in sen.lower():
        if i in vow:
            count+=1
    return count    
print(vowelsCount(aString))    

