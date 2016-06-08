#Bubblesort will iterate through a list of unordered numbers
#Then it will compare two numbers and switch their order if needed
#until it has ordered all the numbers from least to largest.
import time
start_time = time.time()
def bubblesort(myList):
  for sort_num in range(len(myList)-1,0,-1):
    for i in range(sort_num): #iterates thru list
      if myList[i]>myList[i+1]: #Compares a list item to its neighbor to see if greater
        temp = myList[i] #use a temp variable and assign value of myList[i]
        myList[i] = myList[i+1]
        myList[i+1]=temp #This holds the data in temp
myList = [68,13,72,95,48,80,53,71,62,32,89,45,84,98,39,78,91,57,61,18,35,25,51,85,43,92,81,38,59,12,73,28,79,93,86,16,63,26,99,37,82,74,94,22,67,96,77,87,21,54,3,56,69,75,11,64,1,46,29,55,4,76,65,7,31,52,20,14,47,66,17,27,42,100,30,97,33,88,49,83,3,90,34,70,19,40,50,58,60,2,6,8,9,10,23,36,41,15,24] #my list of mixed values to sort
bubblesort(myList)

print(myList)
print("my bubble sort took", time.time() - start_time, "to run")
