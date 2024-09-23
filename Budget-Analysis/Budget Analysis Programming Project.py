#
# Garen Pugmire
# 9-23-24
# Budget Analysis Programming Project
# COSC 2409 DNT
#
# Initializing variables
total = 0
budget = 0
keep_going = 0
difference = 0

# Asking for the budget
budget = int(input('What is your budget for the month? '))

# Asking for expenses and adding to a total
while keep_going == 0 :
    print('Enter an expense amount from this month (Enter "0" when done):')
    expense = int(input())
    total += expense
    if expense == 0 :
        keep_going = 1

# Display budget
if total > budget :
    difference = total - budget
    print('You are $',difference, 'over budget.')
if total < budget :
    difference = budget - total
    print('You are $',difference, 'under budget.')
if total == budget :
    print('You are exactly on budget.')