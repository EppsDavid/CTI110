# CTI 110
# P2T1-Sales Prediction
# David Epps
# July 1, 2018

##A company has determined that its annual profit is
##typically 23 percent of total sales.
##Write a program that asks the user to
##enter the projected amount of total sales, and
##then displays the profit that will be made from that amount.


total_sales = float(input("Enter the projected sales: "))

profit = total_sales * 0.23

print("The profit is $", format(profit, ",.2f"))
