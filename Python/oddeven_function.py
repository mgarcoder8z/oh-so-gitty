def oddeven(first,last):
  for i in range(first,last):
    if i%2==0:
      print("Number is " + str(i) + "." + "This number is even.")
    elif i%2==1:
      print("Number is " + str(i) + "." + "This number is odd.")
oddeven(first=1,last=2000)
