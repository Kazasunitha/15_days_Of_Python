#Create a function that takes a list of dictionaries and sorts them based on a specified key
list1=[
       {"name":"Harini","age":20},
       {"name":"lavanya","age":15},
       {"name":"Prabhas","age":12}
       ]
Key=input("specify the key sort by age or name:")
def sorting(list1,Key):
    print(sorted(list1,key=lambda x:x[Key]))
sorting(list1,Key)    