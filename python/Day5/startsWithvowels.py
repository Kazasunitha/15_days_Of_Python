#Given a list of names, count the number of names that start with a vowel
list1=["orange","apple","banana",",mango"]
vowels=['a','e','i','o','u']
list2=[x for x in list1 if x[0] in vowels]
print(list2)