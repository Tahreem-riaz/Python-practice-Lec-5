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
