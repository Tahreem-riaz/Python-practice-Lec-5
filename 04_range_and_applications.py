"""
========================================================
       LECTURE 05 - FILE 4: RANGE AND APPLICATIONS
========================================================
Topics: range(), for loops, counting, sums,
        multiplication tables, and simple applications
Total Questions: 10
========================================================
"""

# ======================================================
# TOPIC 1: BASIC RANGE
# ======================================================

# ======================================================
# Q1. PRINT NUMBERS
# ======================================================
# Use range() and a for loop to print numbers
# from 1 to 10.

for number in range(1, 11):
    print(number)


# ======================================================
# TOPIC 2: RANGE WITH STEP
# ======================================================

# ======================================================
# Q2. PRINT EVEN NUMBERS
# ======================================================
# Use range() to print even numbers from 2 to 20.
#
# Expected output:
# 2
# 4
# 6
# ...
# 20

for number in range(2, 21, 2):
    print(number)


# ======================================================
# TOPIC 3: RANGE WITH A NEGATIVE STEP
# ======================================================

# ======================================================
# Q3. COUNT BACKWARDS
# ======================================================
# Use range() to print numbers from 10 down to 1.
#
# Expected output:
# 10
# 9
# 8
# ...
# 1

for number in range(10, 0, -1):
    print(number)


# ======================================================
# TOPIC 4: SUM USING RANGE
# ======================================================


# ======================================================
# Q4. SUM OF NUMBERS
# ======================================================
# Use range() and a for loop to calculate
# the sum of numbers from 1 to 10.

total = 0

for number in range(1, 11):
    total += number

print("Sum:", total)   

# ======================================================
# TOPIC 5: COUNTING WITH RANGE
# ======================================================

# ======================================================
# Q5. COUNT MULTIPLES
# ======================================================
# Use range() to print multiples of 5 from
# 5 to 50.
#
# Expected output:
# 5
# 10
# 15
# ...
# 50

for number in range(5, 51, 5):
    print(number)

# ======================================================
# TOPIC 6: MULTIPLICATION TABLE
# ======================================================

# ======================================================
# Q6. MULTIPLICATION TABLE
# ======================================================
# Given:
# number = 7
#
# Use range() and a for loop to print
# the multiplication table of 7 from 1 to 10.

number = 7

for multiplier in range(1, 11):

    result = number * multiplier

print(number, "x", multiplier, "=", result)

# ======================================================
# TOPIC 7: RANGE WITH CONDITIONS
# ======================================================

# ======================================================
# Q7. FIND NUMBERS DIVISIBLE BY 3
# ======================================================
# Use range() to check numbers from 1 to 30.
#
# Print only the numbers that are divisible by 3.

for number in range(1, 31):

    if number % 3 == 0:
        print(number)


# ======================================================
# TOPIC 8: CALCULATE SQUARES
# ======================================================

# ======================================================
# Q8. NUMBER AND ITS SQUARE
# ======================================================
# Use range() to go from 1 to 10.
#
# For each number, display:
#
# Number: 1 Square: 1
# Number: 2 Square: 4
# Number: 3 Square: 9
#
# Continue until 10.

for number in range(1, 11):

    square = number ** 2

    print("Number:", number, "Square:", square)


# ======================================================
# TOPIC 9: FACTORIAL USING RANGE
# ======================================================    

# ======================================================
# Q9. CALCULATE FACTORIAL
# ======================================================
# Given:
# number = 5
#
# Use range() and a for loop to calculate:
#
# 5! = 5 × 4 × 3 × 2 × 1
#
# Display the final factorial.

number = 5

factorial = 1

for value in range(1, number + 1):

    factorial *= value

print("Factorial:", factorial)

# ======================================================
# TOPIC 10: COUNT AND SUM
# ======================================================

# ======================================================
# Q10. POSITIVE NUMBER APPLICATION
# ======================================================
# Use range() to go from 1 to 20.
#
# Use a for loop to:
# a) Count how many numbers are even.
# b) Calculate the sum of even numbers.
#
# Display both results.

even_count = 0
even_sum = 0

for number in range(1, 21):

    if number % 2 == 0:

        even_count += 1
        even_sum += number

print("Even Numbers Count:", even_count)
print("Sum of Even Numbers:", even_sum)
