#Write a function that takes two lists and returns their intersection (common elements)
def intersection(l1,l2):
    l3=[x for x in l1 if x in l2]
    print(l3)
list1=[2,5,8,15,0,23]  
list2=[1,4,3,6,8,2,19]
intersection(list1,list2)
  