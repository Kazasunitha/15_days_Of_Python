#Given a list of names, print all names starting with the letter 'A'
n=int(input("Enter the no of elements of lists:"))
l=[]
for i in range(n):
    a=input()
    l.append(a.upper())
print(l)  
for word in l:
    if word[0]=='A':
        print(word)  

