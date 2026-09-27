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
    
     