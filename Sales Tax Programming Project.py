#
# Name
# Date
# Sales Tax Programming Project
# COSC 2409 DNT
#

# Variable declarations

# Constants for the state and county tax rates

# Get the amount of the purchase.
purchase_amount = float(input('Enter the amount of the purchase: '))
# Calculate the state sales tax.
state_tax = purchase_amount * .05
# Calculate the county sales tax.
county_tax = purchase_amount * .025
# Calculate the total tax.
total_tax = purchase_amount * .075
# Calculate the total of the sale.
total_amount = purchase_amount + total_tax
# Print information about the sale.
print('Purchase: $', format(purchase_amount, ',.2f'))
print('State Sales Tax: $', format(state_tax, ',.2f'))
print('County Sales Tax: $', format(county_tax, ',.2f'))
print('Total Sales Tax: $', format(total_tax, ',.2f'))
print('Total: $', format(total_amount, ',.2f'))
