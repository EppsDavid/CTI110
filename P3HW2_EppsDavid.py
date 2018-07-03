#CTI-110
# P3HW2
# David Epps
# June 21,2018

# Write a Program tha asks the user to enter the number of packages purchased.
# The progam should then display the amount of the discount(if any)
# and the total cost with the discount applied.

# Quantity 10-19: 10% discount
# Quantity 20-49: 20% discount
# Quantity 50-99: 30% discount
# Quantity 100+: 40% discount

quantity = int(input("Enter the number of packages you purchased: "))

             


if quantity < 10:
    print("There is no discount")
    print((quantity*99))
elif quantity >=10 and quantity <=19:
    print("You have a 10% discount")
    print((quantity*99)*0.10)
elif quantity >=20 and quantity <=49:
    print("You have a 20% discount")
    print ((quantity*99)*0.20)
elif quantity >=50 and quantity <=99:
    print("You have a 30% discount")
    print((quantity*99)*0.30)
elif quantity >=100:
    print("You have a 40% discount")
    print((quantity*99)*0.40)

    
