# CTI-110
# P3Lab
# David Epps
# June 21, 2018



# Use the if/else structure to determine the letter grade
# Get input from the user

grade = int(input( "Enter a numberic grade from 0 to 100:"))

if grade > 89:
    print(" You made an A!")
    print("Your numeric grade",grade,"is an A!")
elif grade > 79:
    print(" You made an B!")
    print("Your numeric grade",grade,"is an B!")
elif grade > 69:
    print(" You made an C!")
    print("Your numeric grade",grade,"is an C!")
elif grade > 59:
    print(" You made an D!")
    print("Your numeric grade",grade,"is an D!")
else:
    print(" You made an F!")
    print("Your numeric grade",grade,"is an F!")


