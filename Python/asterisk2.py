from collections import defaultdict

myList=[2,5,"Ron",8,"Harry",15,"Hermione"]

d = defaultdict(list)
for x in myList:
  d[type(x)].append(x)

print (d[int])
newintList=d[int]
for i in range(len(newintList)):
	print(newintList[i]*"*")

print (d[str])
newstringList=d[str]
for i in range(len(newstringList)):
	print([i[0]*len(i) for i in newstringList])
