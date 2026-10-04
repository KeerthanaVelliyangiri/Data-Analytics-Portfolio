class Person:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

class Student(Person):
    def __init__(
        self,
        student_id,
        name,
        email,
        phone,
        department,
        attendance,
        python_marks,
        sql_marks,
        excel_marks):

        # Call Person class constructor
        super().__init__(name, email, phone)

        # Student-specific attributes
        self.student_id = student_id
        self.department = department
        self.attendance = attendance
        self.python_marks = python_marks
        self.sql_marks = sql_marks
        self.excel_marks = excel_marks

    def calculate_total(self):
        total = (self.python_marks + self.sql_marks + self.excel_marks)
        return total
    
    # Calculate Average Marks
    def calculate_average(self):
        total = self.calculate_total()
        average = total / 3
        return average

    # Calculate Result
    def get_result(self):
        average = self.calculate_average()
        if average >= 50:
            return "Passed"
        else:
            return "Failed"

    # Calculate Grade
    def calculate_grade(self):
        average = self.calculate_average()
        if average >= 90:
            return "A+"
        elif average >= 80:
            return "A"
        elif average >= 70:
            return "B"
        elif average >= 60:
            return "C"
        elif average >= 50:
            return "D"
        else:
            return "F"

    # Check Attendance Eligibility
    def check_attendance(self):
        if self.attendance >= 75:
            return "Eligible"
        else:
            return "Not Eligible"

    # Display Student Information
    def display_student_info(self):
        print("Student ID :", self.student_id)
        print("Name       :", self.name)
        print("Email      :", self.email)
        print("Phone      :", self.phone)
        print("Department :", self.department)
        print("Attendance :", self.attendance, "%")
 
    # Display Academic Information
    def display_academic_info(self):
        print("Student ID   :", self.student_id)
        print("Name         :", self.name)
        print("Department   :", self.department)
        print("Python Marks :", self.python_marks)
        print("SQL Marks    :", self.sql_marks)
        print("Excel Marks  :", self.excel_marks)
        print("Total Marks  :", self.calculate_total())
        print("Average Marks:",round(self.calculate_average(), 2))
        print("Result       :", self.get_result())
        print("Grade        :", self.calculate_grade())
        print("Attendance   :", self.attendance, "%")
        print("Exam Status  :",self.check_attendance())

# Faculty also inherits from Person.
# It contains faculty-specific information.
class Faculty(Person):
    def __init__(
        self,
        faculty_id,
        name,
        email,
        phone,
        department,
        designation
    ):

        # Call Person class constructor
        super().__init__(name, email, phone)

        # Faculty-specific attributes
        self.faculty_id = faculty_id
        self.department = department
        self.designation = designation

    # Display Faculty Information
    def display_faculty_info(self):
        print("Faculty ID  :", self.faculty_id)
        print("Name        :", self.name)
        print("Email       :", self.email)
        print("Phone       :", self.phone)
        print("Department  :", self.department)
        print("Designation :", self.designation)

# University class manages multiple students and faculty
class University:
    def __init__(self):
        # List to store multiple student objects
        self.students = []
        # List to store multiple faculty objects
        self.faculty_members = []

    def add_student(self):
        student_id = input("Enter Student ID: ")
        # Check duplicate Student ID
        for student in self.students:
            if student.student_id == student_id:
                print("Student ID already exists.")
                return
        name = input("Enter Name: ")
        email = input("Enter Email: ")
        phone = input("Enter Phone: ")
        department = input("Enter Department: ")

        try:
            attendance = float(input("Enter Attendance (%): "))
        except ValueError:
            print("Invalid input.")
            print("Attendance must be a number.")
            return

        # Attendance validation
        if attendance < 0 or attendance > 100:
            print("Invalid attendance." " Attendance must be between 0 and 100.")
            return

        try:
            python_marks = float(input("Enter Python Marks: "))
            sql_marks = float(input("Enter SQL Marks: "))
            excel_marks = float(input("Enter Excel Marks: "))

        except ValueError:
            print("Invalid marks.")
            print("Marks must be numeric values.")
            return

        if (
            python_marks < 0
            or python_marks > 100
            or sql_marks < 0
            or sql_marks > 100
            or excel_marks < 0
            or excel_marks > 100
        ):
            print("Invalid marks."" Marks must be between 0 and 100.")
            return
        
        student = Student(
            student_id,
            name,
            email,
            phone,
            department,
            attendance,
            python_marks,
            sql_marks,
            excel_marks
        )

        # Add student to list
        self.students.append(student)
        print("\nStudent added successfully!")

    # view students
    def view_students(self):
        if len(self.students) == 0:
            print("\nNo students available.")
            return
        for student in self.students:
            print(student.student_id,"-",student.name,"-",student.department)

    def check_attendance(self):
        if len(self.students) == 0:
            print("\nNo students available.")
            return
        student_id = input("\nEnter Student ID: ")

        for student in self.students:
            if student.student_id == student_id:

                print("Student Name :", student.name)
                print("Attendance   :",student.attendance,"%")
                print("Exam Status  :",student.check_attendance())
                return
        print("\nStudent not found.")

    def view_result(self):

        if len(self.students) == 0:
            print("\nNo students available.")
            return

        student_id = input("\nEnter Student ID: ")
        for student in self.students:
            if student.student_id == student_id:
                student.display_academic_info()
                return
        print("\nStudent not found.")

    def add_faculty(self):
        faculty_id = input("Enter Faculty ID: ")
        # Check duplicate Faculty ID
        for faculty in self.faculty_members:
            if faculty.faculty_id == faculty_id:
                print("Faculty ID already exists.")
                return

        name = input("Enter Name: ")
        email = input("Enter Email: ")
        phone = input("Enter Phone: ")
        department = input("Enter Department: ")
        designation = input("Enter Designation: ")

        # Create Faculty object
        faculty = Faculty(
            faculty_id,
            name,
            email,
            phone,
            department,
            designation
        )

        # Add faculty object to list
        self.faculty_members.append(faculty)
        print("\nFaculty added successfully!")

    def view_faculty(self):
        if len(self.faculty_members) == 0:
            print("\nNo faculty members available.")
            return

        for faculty in self.faculty_members:
            faculty.display_faculty_info()

    def run(self):

        while True:
            print("NOVA UNIVERSITY STUDENT MANAGEMENT SYSTEM")
            print("1. Add Student")
            print("2. View Students")
            print("3. Check Attendance Eligibility")
            print("4. View Academic Result")
            print("5. Add Faculty")
            print("6. View Faculty")
            print("7. Exit")

            choice = input("Enter your choice: ")
            # Option 1
            if choice == "1":
                self.add_student()

            # Option 2
            elif choice == "2":
                self.view_students()

            # Option 3
            elif choice == "3":
                self.check_attendance()

            # Option 4
            elif choice == "4":
                self.view_result()

            # Option 5
            elif choice == "5":
                self.add_faculty()

            # Option 6
            elif choice == "6":
                self.view_faculty()

            # Option 7
            elif choice == "7":
                print("\nThank you for using " "Nova University Student Management System.")
                break

            # Invalid Menu Choice
            else:
                print("\nInvalid choice."" Please enter a number from 1 to 7.")

# Program call
university = University()
university.run()