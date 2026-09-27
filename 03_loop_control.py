"""
========================================================
          LECTURE 05 - FILE 3: LOOP CONTROL
========================================================
Topics: break, continue, pass, and loop control
Total Questions: 10
========================================================
"""

# ======================================================
# TOPIC 1: BREAK
# ======================================================

# ======================================================
# Q1. STOP AT A SPECIFIC NUMBER
# ======================================================
# Use a for loop to print numbers from 1 to 10.
# Stop the loop when the number reaches 6.
#
# Expected output:
# 1
# 2
# 3
# 4
# 5

for number in range(1, 11):

    if number == 6:
        break

    print(number)


# ======================================================
# TOPIC 2: BREAK WITH A LIST
# ======================================================

# ======================================================
# Q2. FIND A NUMBER
# ======================================================
# Given:
# numbers = [10, 25, 7, 18, 30, 12]
#
# Use a for loop to search for 18.
# Print the numbers while searching.
# Stop the loop when 18 is found.

numbers = [10, 25, 7, 18, 30, 12]

for number in numbers:

    print("Checking:", number)

    if number == 18:
        print("Number Found!")
        break


# ======================================================
# TOPIC 3: BREAK WITH STRINGS
# ======================================================   

# ======================================================
# Q3. STOP AT A LETTER
# ======================================================
# Given:
# letters = ["A", "B", "C", "D", "E", "F"]
#
# Use a for loop to print each letter.
# Stop when the letter is "D".

letters = ["A", "B", "C", "D", "E", "F"]

for letter in letters:

    if letter == "D":
        break

    print(letter)


# ======================================================
# TOPIC 4: CONTINUE WITH A LIST
# ======================================================

# ======================================================
# Q5. SKIP NEGATIVE NUMBERS
# ======================================================
# Given:
# numbers = [10, -5, 8, -2, 15, -7, 20]
#
# Use a for loop to print only positive numbers.
# Use continue to skip negative numbers.

numbers = [10, -5, 8, -2, 15, -7, 20]

for number in numbers:

    if number < 0:
        continue

    print(number)

# ======================================================
# TOPIC 5: BREAK AND CONTINUE TOGETHER
# ======================================================

# ======================================================
# Q5. PRINT POSITIVE NUMBERS UNTIL 20
# ======================================================
# Given:
# numbers = [5, -2, 8, 0, 12, -4, 20, 25, 7]
#
# Use a for loop to:
# a) Skip negative numbers and zero.
# b) Stop when the number is 20.
# c) Print the other numbers.

numbers = [5, -2, 8, 0, 12, -4, 20, 25, 7]
