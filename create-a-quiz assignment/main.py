# Quiz Assingment

# Variables
total = 0

# Question 1
print("Question 1: What is the second color of the rainbow?")
print("Red")
print("Purple")
print("Orange")
print("Yellow")
answer1 = input("Please input your answer").lower()

if (answer1 == "orange"):
    print("CORRECT!")
    total += 1
else:
    print("Sorry that is incorrect")

# Question 2
print("Question 2: Which country has the largest population?")
print("China")
print("India")
print("United States")
print("Russia")
answer2 = input("Please input your answer").lower()

if (answer2 == "china"):
    print("That is correct!")
    total += 1
else:
    print("Better luck next time!")

# Question 3
print("What color does purple and yellow create when mixed?")
print("Red")
print("Black")
print("Blue")
print("Brown")
answer3 = input("Please input your answer").lower()

if(answer3 == "brown"):
    print("That is right!")
    total += 1
else:
    print("That is wrong!")

# Question 4
print("Which of the following is considered the largest organ?"),
print("Liver"),
print("Skin"),
print("Lungs")
print("Heart")
answer4 = input("Please input your answer").lower()

if(answer4 == "skin"):
    print("You got it!")
    total += 1
else:
    print("Unforunately you didn't get it!")

# Calculate Percentage
percentage = 0
if (total == 0):
    percentage = 0
elif (total == 1):
    percentage = 25
elif (total == 2):
    percentage = 50
elif (total == 3):
    percentage = 75
elif (total == 4):
    percentage = 100

# Print Results
print("Your score is " + str(total) + "/4..." + str(percentage) + "%")

# Feedback based on score
if (total == 0):
    print("That's kind of disappointing...")
elif (total == 1):
    print("Better than nothing")
elif (total == 2):
    print("Your half way there!")
elif (total == 3):
    print("Hey atleast you didn't fail!")
elif (total == 4):
    print("Genius right there!")