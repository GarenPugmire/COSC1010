#
# Garen Pugmire
# 9-30-24
# Feet to Inches Programming Project
# COSC 2409 DNT
#
# Use comments liberally throughout the program.
conversion = 12

# Main function:
def main(): 
    # Get a number of feet.
    feet = int(input('Enter a number of feet: '))

    # Convert to inches.
    print(feet, 'equals', feet_to_inches(feet), 'inches.')

# Convert feet to inches.
def feet_to_inches (feet) :
    return feet * conversion

#Call main function.
main ()

