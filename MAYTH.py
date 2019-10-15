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
