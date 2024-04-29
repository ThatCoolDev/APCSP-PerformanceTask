## program for APCSP performance task that I made.
def add_assignment(assignments):
    """
    Function to add an assignment to the list.

    - Takes the assignments list as a parameter.
    - Prompts for assignment name.
    - Appends the assignment to the list.
    """
    name = input("Enter assignment name: ")
    assignment = name
    assignments.append(assignment)

    print("Assignment added successfully.\n")

def display_assignments(assignments):
    """
    Function to display the list of assignments with numbers.
    - Takes the assignments list as a parameter.
    - Prints each assignment with a corresponding number.
    """
    if not assignments:
        print("No assignments added yet.")
        print("Please add an assignment!")
        return

    print("Assignments:")
    for i, assignment in enumerate(assignments, start=1): 
        print(f"{i}. {assignment}")  # Use f-string for formatted output (formatted string)


def main(): # Main function
    assignments = []  # list to store assignments

    while True:
        # Display menu options
        print("Assignment List App\n")
        print("(1) Add Assignment\n")
        print("(2) Display Assignments\n")
        print("(3) Exit\n")

        # Get user input
        choice = input("Enter your choice: ") 

        # Process user input (and detect invalid inputs as well.)
        if choice == '1':
            add_assignment(assignments)
        elif choice == '2':
            display_assignments(assignments)
        elif choice == '3':
            print("Thanks for using my program!")
            break
        else:
            print("Invalid option. Please try again.\n")

if __name__ == "__main__":
    main()