#* Implement a function that takes two lists and returns their union (all unique elements from both lists).
def union(l1,l2):
     l=list(set(l1) | set(l2)) # list1 + list2 is used for union of lists
     return l
l1=[2,4,6,2,19]
l2=[11,8,2,4]
print(union(l1,l2))