maths_marks = 80
python_marks = 90
english_marks = 75

#add
total_marks = maths_marks + python_marks + english_marks

#div
avg_marks = total_marks / 3

# Remainfee
total_fee = 50000
paid_fee = 30000
remain_fee = total_fee - paid_fee

# Compare
py_high = python_marks > maths_marks

# Logical
age = 22
attendance = 85

eligible = age >= 18 and attendance >= 75

# Assignment
up_marks = maths_marks
up_marks += 5


print("Total Marks:", total_marks)
print("Average Marks:", avg_marks)
print("Remaining Fee:", remain_fee)
print("Python mark higher than Maths mark?:", py_high)
print("student eligible?:", eligible)
print("Updated Maths Marks:", up_marks)