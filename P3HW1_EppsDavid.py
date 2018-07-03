# CTI-110
# P3HW1
# David Epps
# June 21, 2018

# Get input from user to determine if person is an infant, a child, a teenager, or and adult.

age= int(input("Enter your age: "))

if age <= 1 : 
    print("You are an Infant")
elif age > 1 and age < 13:
    print("You are a Child")
elif age > 12 and age < 20:
    print("You are a Teenager")
else:
    print("You are an Adult")
    
