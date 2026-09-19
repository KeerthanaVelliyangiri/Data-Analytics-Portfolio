# Student Details
student_id = input("Enter Student ID: ")
student_name = input("Enter Student Name: ")

print("ID   :", student_id)
print("Name :", student_name)

#Menu
while True:
    print("1. Eligibility")
    print("2. Result and Grade")
    print("3. Department Selection")
    print("4. Exit")

    choice = int(input("Choose a service: "))

    # Eligibility
    if choice == 1:

        attendance = float(input("Enter attendance percentage: "))

        if attendance < 0 or attendance > 100:
            print("Invalid attendance. Enter a value from 0 to 100.")

        elif attendance >= 75:
            print("Attendance:", attendance, "%")
            print("Status: Eligible for examination")

        else:
            print("Attendance:", attendance, "%")
            print("Status: Not eligible for examination")

    # Check Result
    elif choice == 2:

        marks = float(input("Enter marks: "))

        if marks < 0 or marks > 100:
            print("Invalid marks. Enter a value from 0 to 100.")

        else:

            # Pass or Fail
            if marks >= 40:
                result = "Pass"
            else:
                result = "Fail"

            # Grade
            if marks >= 90:
                grade = "A"
            elif marks >= 80:
                grade = "B"
            elif marks >= 70:
                grade = "C"
            elif marks >= 60:
                grade = "D"
            elif marks >= 50:
                grade = "E"
            else:
                grade = "F"

            print("Marks  :", marks)
            print("Result :", result)
            print("Grade  :", grade)

    # Department
    elif choice == 3:

        print("1. CSE   - Computer Science & Engineering")
        print("2. IT    - Information Technology")
        print("3. AI&DS - Artificial Intelligence & Data Science")
        print("4. ECE   - Electronics & Communication Engineering")
        print("5. BBA   - Business Administration")

        department = int(input("Select department: "))

        match department:

            case 1:
                print("Selected: Computer Science & Engineering")

            case 2:
                print("Selected: Information Technology")

            case 3:
                print("Selected: Artificial Intelligence & Data Science")

            case 4:
                print("Selected: Electronics & Communication Engineering")

            case 5:
                print("Selected: Business Administration")

            case _:
                print("Invalid department selection.")

    # Exit
    elif choice == 4:

        print("\nThank you for using Nova University Student Service Portal.")
        print("Application closed.")
        break

    # Invalid Service
    else:

        print("Invalid service choice.")
        print("Please select a number from 1 to 4.")
        continue