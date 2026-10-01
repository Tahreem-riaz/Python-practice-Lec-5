"""
========================================================
        LECTURE 05 - FILE 6: MINI PROJECT
========================================================
Project: Simple To-Do List

Concepts Used:
- while loops
- for loops
- range()
- break
- continue
- lists
- conditions
- user input
========================================================
"""

# ======================================================
# SIMPLE TO-DO LIST
# ======================================================

tasks = []

# Keep showing the menu until the user exits.
while True:

    print("\n" + "=" * 35)
    print("          TO-DO LIST")
    print("=" * 35)

    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("\nEnter your choice: ")


# ==================================================
# ADD TASK
# ==================================================
    if choice == "1":

        task = input("Enter a task: ")

        tasks.append(task)

        print("Task added successfully!")


# ==================================================
# VIEW TASKS
# ==================================================

    elif choice == "2":

        print("\n--- YOUR TASKS ---")

        if len(tasks) == 0:

            print("No tasks available.")
        else:

            # Use range() to number the tasks.
            for number in range(len(tasks)):

                print(
                    number + 1,
                    ".",
                    tasks[number]
                )

# ==================================================
# REMOVE TASK
# ==================================================

    elif choice == "3":

        if len(tasks) == 0:

            print("There are no tasks to remove.")
            continue

        print("\n--- YOUR TASKS ---")

        for number in range(len(tasks)):

            print(
                number + 1,
                ".",
                tasks[number]
            )

        task_number = input(
            "Enter task number to remove: "
        )