print("Hello World")
print('Name: Arun \nAge: 21 \nDegree: B.sc (Computer Science)')
Name="Arun"
Age=21
roll_no='101'
print("name",Name)
name2=input("enter student name: ")
print(name2)
print("The name of second student name",name2)
print(f"The name of second student name {name2} and the age of first student is: {Age} ")

# Day 1 - Task

name1 = "Arun"
age1 = 21
roll_no1 = 101
course_name1 = "Python"
course_code1 = "PY101"
no_of_credits1 = 4
course_duration1 = 12

name2 = "Keerthana"
age2 = 22
roll_no2 = 102
course_name2 = "Data Analytics"
course_code2 = "DA101"
no_of_credits2 = 5
course_duration2 = 16

name3 = "Surya"
age3 = 21
roll_no3 = 103
course_name3 = "Java"
course_code3 = "JA101"
no_of_credits3 = 4
course_duration3 = 14

name4 = "Vicky"
age4 = 22
roll_no4 = 104
course_name4 = "SQL"
course_code4 = "SQL101"
no_of_credits4 = 3
course_duration4 = 10

name5 = "Renu"
age5 = 21
roll_no5 = 105
course_name5 = "Power BI"
course_code5 = "PB101"
no_of_credits5 = 4
course_duration5 = 12

# using list

student1 = ["Arun", 21, 101, "Python", "PY101", 4, 12]
student2 = ["Keerthana", 22, 102, "Data Analytics", "DA101", 5, 16]
student3 = ["Surya", 21, 103, "Java", "JA101", 4, 14]
student4 = ["Vicky", 22, 104, "SQL", "SQL101", 3, 10]
student5 = ["Renu", 21, 105, "Power BI", "PB101", 4, 12]

print(student1[0])

#using dictionary

student1 = {
    "Name": "Arun",
    "Age": 21,
    "Roll_no": 101,
    "Course_name": "Python",
    "Course_code": "PY101",
    "No_of_credits": 4,
    "Course_duration": 12
}

student2 = {
    "Name": "Keerthana",
    "Age": 22,
    "Roll_no": 102,
    "Course_name": "Data Analytics",
    "Course_code": "DA101",
    "No_of_credits": 5,
    "Course_duration": 16
}

student3 = {
    "Name": "Surya",
    "Age": 21,
    "Roll_no": 103,
    "Course_name": "Java",
    "Course_code": "JA101",
    "No_of_credits": 4,
    "Course_duration": 14
}

student4 = {
    "Name": "Vicky",
    "Age": 22,
    "Roll_no": 104,
    "Course_name": "SQL",
    "Course_code": "SQL101",
    "No_of_credits": 3,
    "Course_duration": 10
}

student5 = {
    "Name": "Renu",
    "Age": 21,
    "Roll_no": 105,
    "Course_name": "Power BI",
    "Course_code": "PB101",
    "No_of_credits": 4,
    "Course_duration": 12
}

print(student2["Name"])