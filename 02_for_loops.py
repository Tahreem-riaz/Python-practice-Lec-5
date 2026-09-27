"""
========================================================

          LECTURE 05 - FILE 2: FOR LOOPS
========================================================
Topics: for loops, nested loops, lists, tuples,
        strings, range, counters, calculations
Total Questions: 10
========================================================
"""

# ======================================================
# TOPIC 1: FOR LOOPS WITH LISTS AND CALCULATIONS
# ======================================================

# ======================================================
# Q1. STUDENT RESULT ANALYZER
# ======================================================
# Given:
# marks = [78, 45, 92, 33, 86, 59, 71, 28]
#
# Use a for loop to:
# a) Print each student's marks with numbering.
# b) Count how many students passed (marks >= 50).
# c) Find the highest and lowest marks.
# d) Calculate the class average.

marks = [78, 45, 92, 33, 86, 59, 71, 28]

passed_students = 0
total_marks = 0
highest_marks = marks[0]
lowest_marks = marks[0]

# Loop through the marks with student numbering.
for number, mark in enumerate(marks, start=1):

    # Display each student's marks.
    print("Student", number, ":", mark)

     # Add each mark to the total.
    total_marks += mark

    # Count students who passed.
    if mark >= 50:
        passed_students += 1

    # Check for the highest mark.
    if mark > highest_marks:
        highest_marks = mark

    # Check for the lowest mark.
    if mark < lowest_marks:
        lowest_marks = mark

# Calculate the class average.
average = total_marks / len(marks)    

print("Passed Students:", passed_students)
print("Highest Marks:", highest_marks)
print("Lowest Marks:", lowest_marks)
print("Class Average:", average)


# ======================================================
# TOPIC 2: FOR LOOPS WITH STRINGS
# ======================================================

# ======================================================
# Q2. CHARACTER FREQUENCY ANALYZER
# ======================================================
# Given:
# text = "programming is a powerful skill"
#
# Use a for loop to:
# a) Count vowels and consonants separately.
# b) Ignore spaces.
# c) Count how many times each vowel occurs.
# d) Display the total number of letters.

text = "programming is a powerful skill"

vowels = "aeiou"

vowel_count = 0
consonant_count = 0
letter_count = 0

# Create a dictionary to store the frequency of each vowel.
vowel_frequency = {
    "a": 0,
    "e": 0,
    "i": 0,
    "o": 0,
    "u": 0
}

# Loop through every character in the text.
for character in text.lower():

    # Ignore spaces.
    if character == " ":
        continue

# Process only alphabetic characters.
    if character.isalpha():

       # Count the total number of letters.
        letter_count += 1

       # Check whether the character is a vowel.
        if character in vowels:
            vowel_count += 1
            vowel_frequency[character] += 1

         # Otherwise, it is a consonant.
        else:
            consonant_count += 1

print("Vowels:", vowel_count)
print("Consonants:", consonant_count)
print("Total Letters:", letter_count)
print("Vowel Frequency:", vowel_frequency)


# ======================================================
# TOPIC 3: BASIC FOR LOOPS WITH NUMBERS
# ======================================================

# ======================================================
# Q3. NUMBER SQUARES
# ======================================================
# Given:
# numbers = [2, 4, 6, 8, 10]
#
# Use a for loop to:
# a) Print each number.
# b) Calculate and print its square.
#
# Example:
# Number: 2 Square: 4

numbers = [2, 4, 6, 8, 10]

# Loop through each number.
for number in numbers:

    # Calculate the square.
    square = number ** 2

print("Number:", number, "Square:", square)

# ======================================================
# TOPIC 4: FOR LOOPS WITH CONDITIONS
# ======================================================

# ======================================================
# Q4. EVEN AND ODD NUMBERS
# ======================================================
# Given:
# numbers = [12, 7, 18, 5, 20, 9, 14, 3]
#
# Use a for loop to:
# a) Check each number.
# b) Display whether the number is even or odd.

numbers = [12, 7, 18, 5, 20, 9, 14, 3]

# Check each number.
for number in numbers:

    if number % 2 == 0:
        print(number, "is Even")
    else:
        print(number, "is Odd")


# ======================================================
# TOPIC 5: FOR LOOPS WITH COUNTERS
# ======================================================