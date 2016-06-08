import time
start_time = time.time()
def selectionSort(myList):
  for checkSlot in range(len(myList)-1,0,-1):
    placeofMax = 0
    for location in range(1,checkSlot+1):
      if myList[location]>myList[placeofMax]:
        placeofMax = location

    temp = myList[checkSlot]
    myList[checkSlot] = myList[placeofMax]
    myList[placeofMax] = temp

myList = [68,13,72,95,48,80,53,71,62,32,89,45,84,98,39,78,91,57,61,18,35,25,51,85,43,92,81,38,59,12,73,28,79,93,86,16,63,26,99,37,82,74,94,22,67,96,77,87,21,54,3,56,69,75,11,64,1,46,29,55,4,76,65,7,31,52,20,14,47,66,17,27,42,100,30,97,33,88,49,83,3,90,34,70,19,40,50,58,60,2,6,8,9,10,23,36,41,15,24] #my list of mixed values to sort

selectionSort(myList)
print(myList)
print("my selection sort took", time.time() - start_time, "to run")
