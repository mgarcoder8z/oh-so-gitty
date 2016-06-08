score=0
for i in xrange(1,11):
	score=int(raw_input("Enter a score between 0 and 100: "))

	if score >= 90 and score <= 100:
		print(str(score) + "," + "Your grade is an A")
	elif score >= 80 and score <= 89:
		print(str(score) + "," + "Your grade  is an B")
	elif score >= 70 and score <= 79:
		print(str(score) + "," + "Your grade  is an C")
	elif score >= 60 and score <= 69:
		print(str(score) + "," + "Your grade  is an D")
	elif score >= 50 and score <= 59:
		print(str(score) + "," + "Your grade is an F")
