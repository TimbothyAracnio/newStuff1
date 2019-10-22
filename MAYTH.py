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
num = 0
for val in range(1, 201, 2):
    acc = acc + val
    num = (val - (val - 1)) + num
print(acc / num)



# Write a function that returns the average of the first N numbers, where
#   N is a parameter
# This takes the average of the all of the numbers chosen in variable N
def inpoot(N):
    acc = 0
    for val in range(0, N, 1):
        acc = acc + val
    print(acc/N)

inpoot(8)

# Write a function called factorial that computes the product of the first N
#   numbers, where N is a parameter
def factorial(N):
    acc = 0
    for val in range(0, N, 1):
        acc = acc * val
    print(acc)

factorial(1)


# Monte Carlo Simulation


# random numbers

import random

print(random.random())

# Boolean Expression
# <, <=, >, >=, ==, !=.
# Compound statements
# and, or, not

dogeFatness = 18
print(dogeFatness > 25)
horseFatness = 215

# if the statement is "and", both of the statements have to be true,
#   otherwise it's false
print(dogeFatness == 45 and horseFatness == 215)

# if the statement is "or", either of the statements have to be true,
#   otherwise it's false
print(dogeFatness >= 25 or horseFatness >= 10)

# if the statement is "not", it flips the answer from true to false and vise versa
print(not horseFatness <= 200)

# Decision making skills

jeff = 19
amy = 16
harold = 23
andy = 20
rebbekah = 19
ans = 0

# now we put else into the kahooky
if jeff < 19:
    if rebbekah >= 10:
        ans = 300
    else:
        print("slippy slap")
else:
    ans = 400

print(ans)

# elif if you want to stack if statements
thingy = 75
if thingy > 100:
    print("bigger than 100")
elif thingy > 80:
    print("bigger than 80")
elif thingy > 45:
    print("bigger than 45")
else:
    print("bigger than a lot.")


def montePi(numDarts):

    inCircle = 0

    for i in range(numDarts):
        x = random.random()
        y = random.random()

        distance = math.sqrt(x**2 + y**2)
        if distance <= 1:
            inCircle = inCircle + 1

    pi = inCircle / numDarts * 4
    return pi