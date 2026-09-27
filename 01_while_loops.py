"""
========================================================
          LECTURE 05 - FILE 1: WHILE LOOPS
========================================================
Topics: while loop, conditions, counters, user input
Total Questions: 10
========================================================
"""

# ==========================================
# PART A: BASIC WHILE LOOP
# ==========================================

# Q1. Password Retry System
#
# Create a program that asks the user to enter
# a password.
#
# Keep asking until the correct password is entered.
#
# Display:
# - "Incorrect Password" for a wrong password
# - "Access Granted" when the password is correct


correct_password = "python123"

# Start with an empty password.
password = ""

# Keep running while the password is incorrect.
while password != correct_password:

 password = input("Enter your password: ")

 # Check if the entered password is correct.
    if password == correct_password:
        print("Access Granted!")
    else:
        print("Incorrect Password. Try again.")

print("Welcome to the system!")

# ------------------------------------------

# Q2. Student Marks Entry
#
# Create a program that keeps asking the user
# to enter marks.
#
# Stop when the user enters -1.
#
# After stopping, display:
# - Total marks
# - Number of subjects

print("\nQ2. Student Marks Entry")

total_marks = 0
subject_count = 0

marks = int(input("Enter marks (-1 to stop): "))

while marks != -1:

# Add the marks to the total.
total_marks += marks

# Count the subject.
subject_count += 1

 marks = int(input("Enter marks (-1 to stop): "))

print("Total Marks:", total_marks)
print("Number of Subjects:", subject_count)

# ------------------------------------------

# Q3. ATM PIN Verification
#
# Create a program that asks the user to enter
# a four-digit PIN.
#
# Keep asking until the correct PIN is entered.
#
# Display "PIN Accepted" when the correct PIN
# is entered.

correct_pin = "1234"
pin = ""

# Keep asking while the PIN is incorrect.
while pin != correct_pin:

    pin = input("Enter your four-digit PIN: ")

  # Check whether the entered PIN is correct.
    if pin == correct_pin:
        print("PIN Accepted")
    else:
        print("Incorrect PIN. Try again.")


# ==========================================
# PART B: COUNTER AND TOTAL
# ==========================================

# Q4. Shopping Total
#
# Create a program that keeps asking the user
# to enter the price of an item.
#
# Enter 0 to stop adding items.
#
# At the end, display the total shopping cost.

total_cost = 0

# Ask for the first item price.
price = float(input("Enter item price (0 to stop): "))

# Continue adding prices until 0 is entered.
while price != 0:

 # Add the item price to the total.
    total_cost += price

# Ask for the next item price.
    price = float(input("Enter item price (0 to stop): "))

print("Total Shopping Cost:", total_cost)

# ------------------------------------------

# Q5. Savings Goal
#
# A student wants to save money for a laptop.
#
# Keep asking the user to enter the amount
# saved each month.
#
# Stop when the total savings reach or exceed
# 100000.
#
# Display the final savings amount.

savings = 0
target = 100000

# Continue taking savings until the target is reached.
while savings < target:

monthly_saving = float(input("Enter amount saved this month: "))

# Add the monthly saving to the total.
savings += monthly_saving

print("Current Savings:", savings)

print("Savings Goal Reached!")
print("Final Savings:", savings)

# ==========================================
# PART C: NUMBER PROCESSING
# ==========================================

# Q6. Positive Number Counter
#
# Keep asking the user to enter numbers.
#
# Stop when the user enters 0.
#
# Count how many positive numbers were entered.
#
# Display the final count.

positive_count = 0

# Ask for the first number.
number = int(input("Enter a number (0 to stop): "))

# Continue until 0 is entered.
while number != 0:

# Check if the number is positive.
    if number > 0:
        positive_count += 1

 # Ask for the next number.
    number = int(input("Enter a number (0 to stop): "))

print("Positive Numbers:", positive_count)

# ------------------------------------------

# Q7. Number Sum Calculator
#
# Keep asking the user to enter numbers.
#
# Stop when the user enters -1.
#
# Calculate and display the sum of all
# entered numbers.
#
# Write your code below:

total = 0

# Ask for the first number.
number = int(input("Enter a number (-1 to stop): "))

# Continue until -1 is entered.
while number != -1:

# Add the number to the total.
total += number

 # Ask for the next number.
number = int(input("Enter a number (-1 to stop): "))

print("Sum of Numbers:", total)

# ==========================================
# PART D: REAL-LIFE APPLICATIONS
# ==========================================
