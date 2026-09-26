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

