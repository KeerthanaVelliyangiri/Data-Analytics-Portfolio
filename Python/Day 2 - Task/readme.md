The **Student Service Portal** is a console-based Python application developed as part of the Day 2 Python Activity at Nova University.

The application allows students to enter their details and perform common academic services such as checking examination eligibility, viewing result and grade, and selecting a department.

## 🎯 Features

* Student ID and name input
* Examination eligibility check
* Attendance validation
* Result – Pass / Fail
* Grade calculation
* Department selection
* Invalid input handling
* Multiple services in one session
* Exit option

## 🛠️ Concepts Used

* `input()` and `print()`
* Variables and data types
* Type casting
* `if`, `elif`, and `else`
* `while` loop
* `match` statement
* `break` and `continue`
* Input validation

## 📋 Business Rules

### Examination Eligibility

* Attendance must be between `0` and `100`.
* `75%` or above → Eligible
* Below `75%` → Not Eligible

### Result

* Marks must be between `0` and `100`.
* `40` or above → Pass
* Below `40` → Fail

### Grade

| Marks    | Grade |
| -------- | ----- |
| 90–100   | A     |
| 80–89    | B     |
| 70–79    | C     |
| 60–69    | D     |
| 50–59    | E     |
| Below 50 | F     |

### Departments

* CSE – Computer Science & Engineering
* IT – Information Technology
* AI&DS – Artificial Intelligence & Data Science
* ECE – Electronics & Communication Engineering
* BBA – Business Administration

## ▶️ How It Works

1. Enter Student ID and Student Name.
2. Select a service from the menu.
3. Provide the required information.
4. The application validates the input.
5. The selected service result is displayed.
6. The menu appears again for another service.
7. Select **Exit** to close the application.

## 📂 Project Structure

```text
nova-university-python-day2/
│
├── README.md
├── student_service_portal.py

```

## 🧪 Testing

The application is tested with:

* Valid and invalid attendance
* Attendance below and above the allowed range
* Marks below, equal to, and above the pass mark
* Different grade ranges
* Valid and invalid department selections
* Invalid service choices
* Multiple services in one session
* Exit option

## 📚 Learning Outcome

This activity helped me understand how **control flow, loops, conditions, input validation, `break`, `continue`, and `match`** can be combined to build a simple interactive Python application.
