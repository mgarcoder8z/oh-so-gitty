# Create empty 'scores' list to hold provided scores
scores = []


# Create function to process grades and provide letter grade
def printGrades(grades):
    # Iterate through provided collection, referring to list as 'grades'
    # and list items as 'grade'
    for grade in grades:
        # Check which range grade falls in and print corresponding letter value
        if grade < 70:
            print("Your grade is {}, your letter grade is D.".format(grade))
        elif grade < 80:
            print("Your grade is {}, your letter grade is C.".format(grade))
        elif grade < 90:
            print("Your grade is {}, your letter grade is B.".format(grade))
        else:
            print("Your grade is {}, your letter grade is A.".format(grade))
    print("Total length of scores collection:", len(scores))


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
            # If user input is not between 60 and 100, print error notice
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
