#Given a list of names, remove all duplicate names and print the unique names$
l=["Prabhas","Rana","Anushka","Tamanna","Dulquer","Prabhas"]
unique=[]
for x in l:
    if(x not in unique):
        unique.append(x)
print(unique)        