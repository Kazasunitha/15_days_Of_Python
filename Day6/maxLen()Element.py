#Given a list of words, find the word with the maximum length and its length$
l=["bahubali","chathrapathi","munna","mr.perfect","saho"]
lenlist=[len(x) for x in l]
a=lenlist.index(max(lenlist))
print(l[a])
print(max(lenlist))