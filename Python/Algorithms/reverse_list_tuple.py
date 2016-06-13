from __future__ import print_function
x = [-3, -2, -1, 0, 1, 2, 3]
#This version does not use a temp variable to hold the index value before switching
#instead the tuple allows you to switch variables
def revlist(aList):
  for i in range(len(aList)/2):
      print("list at start of loop",i,":",aList)
      aList[i],aList[len(aList) - i - 1] = aList[len(aList) - i - 1],aList[i]
      print("list at end of loop  ",i,":",aList)
  return aList

print(revlist(x))
