#
# Garen Pugmire
# September 14, 2024
# Areas of Rectangles Programming Project
# COSC 2409 DNT
#
# Local variables
lengthA = 0.0
lengthB = 0.0
widthA = 0.0
widthB = 0.0
areaA = 0.0
areaB = 0.0
# Get length A
lengthA = int(input('Enter the length of rectangle A: '))
# Get width A
widthA = int(input('Enter the width of rectangle A: '))
# Get length B
lengthB = int(input('Enter the length of rectangle B: '))
# Get width B
widthB = int(input('Enter the width of rectangle B: '))
# Calculate area A
areaA = lengthA * widthA
# Calculate area B
areaB = lengthB * widthB
# Print area comparison using if-elif-else statements
if areaA > areaB:
    print('Rectangle A has a greater area')
elif areaA < areaB:
    print('Rectangle B has a greater area.')
else:
    print('Both rectangles have the same area.')