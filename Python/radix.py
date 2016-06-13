def radixSort(a,n,maxLen):
 for x in range(maxLen):
   bins = [[] for i in range(n)]
   for y in a:
       bins[(y/10**x)%n].append(y)
   a=[]
   for section in bins:
       a.extend(section)
 return a
if __name__=="__main__":
   import random
   a = [random.randint(0,100000) for i in xrange(100)]
   print(radixSort(a,10,5))
