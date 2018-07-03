# CTI 110
# P2HW2-Tip Tax Total
# David Epps
# July 1, 2018

#Write a program that calculates the total cost of a meal purchased at a restaurant.
#The program should ask the user to enter the charge for the food.
#It should then calculate the amount of the tip and the amount for sales tax.
#(Assume 18% tip and 7% sales tax.)
#Display both of these amounts as well as the total cost of the meal. 


foodPrice = float(input("Please enter the amount of the food: "))

tip = 0.18 * foodPrice

salesTax = 0.07 * foodPrice

total = foodPrice + tip + salesTax

print("Food Price " + format( foodPrice, ",.2f"), "Tip: $" + \
      format(tip,",.2f" ), "Sales Tax: $" + format( salesTax, ",.2f"), \
      "Total: $" + format( total, ",.2f"), sep = "\n")
