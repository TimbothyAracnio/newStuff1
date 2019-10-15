# we are going to look at the approximations of Pi
# as well as looking at the math Module

print(22/7)
print(355/113)

import math

print(9801 / (2206 * math.sqrt(2)))

# archimedes Pi:


def archimedes(numSides):
    innerAngleB = 360.0 / numSides
    halfAngleA = innerAngleB / 2
    oneHalfSideS = math.sin(math.radians(halfAngleA))
    sideS = oneHalfSideS * 2
    polygonCircumfrence = numSides * sideS
    pie = polygonCircumfrence / 2
    return pie

print(archimedes(4))
print(archimedes(8))
print(archimedes(16))

for sides in range(8, 1000, 8):
    print(sides, (archimedes(sides) - math.pi))

# See the loop above.  in addition to the value of pi, print the difference
# between the values calculated by the archimedes function and by math.pi.
# How many sides does it take to make the two close?



# Accumulators
# THIS IS NOT ALGEBRA

acc = 0

for val in range(1, 6):
    acc = acc + val

print(acc)
acc = 0


# Compute the sum of the first 100 even numbers
# this is done by repeating the loop and printing the numbers as it loops
for val in range(0, 101, 2):
    acc = acc + val
print(acc)
acc = 0  # Important to set acc back to zero otherwise it might die

# Compute the sum of the first 50 odd numbers
# this is done by pretty much the same thing as above accept adding one to
# the numbers and swapping it from 101 to 51
for val in range(1, 51, 2):
    acc = acc + val
print(acc)
acc = 0


# Compute the average of the first 100 odd numbers
# this takes and adds all of the odd numbers then divides them by how many
# odd numbers there are, giving the average
for val in range(1, 101, 2):
    acc = acc + val
acc / 50

# Write a function that returns the average of the first N numbers, where




