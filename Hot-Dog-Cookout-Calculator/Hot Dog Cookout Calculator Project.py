#
# Garen Pugmire
# September 14, 2024
# Hot Dog Cookout Calculator Programming Project
# COSC 2409 DNT
#
# Declare Variables
people = 0
dogs_each = 0
dog_packages = 0
bun_packages = 0
dogs_total = 0
dogs_left = 0

# Get for the number of people and how many hot dogs they will eat.
people = int(input('How many people will be at the cookout? '))
dogs_each = int(input('How many hot dogs will each person have? '))

# Calculate the number of hot dogs needed.
dogs_total = people * dogs_each

# Calculate the minimum number of packages.
#(I'm adding to the total amount of hot dogs so that the # of packages will round up)
dog_packages = (dogs_total + 4) / 10
bun_packages = (dogs_total + 3) / 8

#Calculate the left over buns and dogs.
#(Had to look up how to use round because I couldn't think of another way to get the right result)
dogs_lo = (round(dog_packages) * 10) - dogs_total
buns_lo = (round(bun_packages) * 8) - dogs_total

# Display the minimun number of packages and the number of dogs and buns left over.
print(f'You will need {dog_packages: .0f} packages of hot dogs;')
print(f'there will be {dogs_lo: .0f} left over.')
print(f'You will need {bun_packages: .0f} packages of buns;')
print(f'there will be {buns_lo: .0f} left over.')
