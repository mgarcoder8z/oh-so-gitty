scores=[] #empty container to hold scores

def printGrades(grades):
    for grade in grades: #where grade is the score and grades is the list
        if grade < 70:
            print("Your grade is {}, your letter grade is D.".format(grade))
        elif grade < 80:
            print("Your grade is {}, your letter grade is C.".format(grade))
        elif grade < 90:
            print("Your grade is {}, your letter grade is B.".format(grade))
        else:
            print("Your grade is {}, your letter grade is A.".format(grade))
print("End of input", len(scores)) #This ends the program and states how many score inputs were given

# Create function to collect scores from user
def getScores():
    # Continue loop while length of scores list is less than 10
    while (len(scores) < 10):
        # Try to get userinput and convert to int
        try:
            userinput = int(raw_input("Please enter a grade between 60 and 100: "))
        # In the case of 'ValueError', print error notice
        except ValueError:
            print("Please provide a whole number input!")
        # Else if successful, confirm input is between 60 and 100
        else:
            if not 60 <= userinput <= 100:
                print("Please provide a whole number between 60 and 100!")
            # Else add score to scores list and print success notice
            else:
                scores.append(userinput)
                print("Score added")
    # After while loop stops (scores list has 10 items), call printGrades function
    # passing scores list as argument
    printGrades(scores)

# Call getScores() function to start collecting user inputs when program is run
getScores()
