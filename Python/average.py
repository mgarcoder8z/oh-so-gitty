def listsum(numList):
    sum=0
    for i in numList:
        sum=sum+i
    return sum
def average(numList):
    return float(sum(numList))/len(numList)
print(average([1,2,5,10,255,3]))
