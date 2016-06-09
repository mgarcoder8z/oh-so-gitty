import time
start_time = time.time() #this will start the clock
def my_sort(myList):
    for i in range(1,len(myList)): #iterates through the list
        val = myList[i] #sets the current value to compare to others
        j = i - 1 #this looks at next number to compare against
        while (j >= 0) and (myList[j] > val): #while the number is positive and it is greater than current value
            myList[j+1] = myList[j] #this shifts the numbers to the right and leaves a slot, doesn't move if ordered already
            j = j - 1
        myList[j+1] = val #this switches the values to sort them in order

myList=[68,13,72,95,48,80,53,71,62,32,89,45,84,98,39,78,91,57,61,18,35,25,51,85,43,92,81,38,59,12,73,28,79,93,86,16,63,26,99,37,82,74,94,22,67,96,77,87,
21,54,3,56,69,75,11,64,1,46,29,55,4,76,65,7,31,52,20,14,47,66,17,27,42,100,30,97,33,88,49,83,3,90,34,70,19,40,50,58,60,2,6,8,9,10,23,36,41,15,
24]

my_sort(myList) #calls the function to start sorting
print(myList) #prints the ordered list
print("my insertion sort took", time.time() - start_time, "to run") #this will stop the clock
