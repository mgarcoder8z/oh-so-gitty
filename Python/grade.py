score=0
for i in xrange(1,11):
	score=int(raw_input("Enter a score between 0 and 100: "))
	if not 0 <= score <=100:
		print("Must enter a number between 0 and 100")
	if score >= 90:
		print(str(score) + "," + "Your grade is an A")
	elif score >= 80:
		print(str(score) + "," + "Your grade  is an B")
	elif score >= 70:
		print(str(score) + "," + "Your grade  is an C")
	elif score >= 60:
		print(str(score) + "," + "Your grade  is an D")
	elif score >= 50:
		print(str(score) + "," + "Failed")
	else:
		print(str(score) + "," + "You must retake the class")
