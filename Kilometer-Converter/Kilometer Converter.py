#
# Garen Pugmire
# 9-30-24
# Kilometer Converter Programming Project
# COSC 2409 DNT
# Variables
CONVERSION_FACTOR = 0.6214
miles = 0
km = 0
kilometers = 0

# Gets distance in km and calls show_miles to convert it.
def main () :
    # Get distance in kilometers.
    kilometers = float(input('Enter a distance in kilometers: '))

    # Display distance converted to miles.
    show_miles(kilometers)

# Converts the parameter km from kilometers to miles and diplays the result.
def show_miles (km) :
    # Calculate miles.
    miles = km * CONVERSION_FACTOR

    # Display miles.
    print(km, 'kilometers equals', miles,'miles.')

# Call main function
main()