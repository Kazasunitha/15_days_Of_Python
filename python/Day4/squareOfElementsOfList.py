#Create a function to find the square of each element in a given list"
l=[2,5,8,19,20,45]
def square(l):
   square=list(map(lambda x:x*x,l))
   print(square)
square(l)   
