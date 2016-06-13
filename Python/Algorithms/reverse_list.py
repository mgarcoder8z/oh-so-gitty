from __future__ import print_function
x = [-3, -2, -1, 0, 1, 2, 3]
#This version uses a temp variable to hold the value of the index so that
#it does not get overwritten by the switch and then overwrites the value with the contents of temp
#to do the switching
def revlist(aList):
  for i in range(len(aList)/2):
      print("list at start of loop",i,":",aList)
      temp = aList[i]
      aList[i] = aList[len(aList) - i - 1]
      aList[len(aList) - i - 1] = temp
      print("list at end of loop  ",i,":",aList)
  return aList

print(revlist(x))
