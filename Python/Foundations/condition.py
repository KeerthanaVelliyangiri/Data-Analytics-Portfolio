mark=int(input("enter your mark : "))
if (mark >= 90):
    print("Grade A")
elif ( mark < 90 and mark >=75 ):
    print("Grade B")
elif ( mark < 75 and mark >=50 ):
    print("Grade C")
else:
    print("Fail")

#task 2
mark=int(input("enter your mark : "))
if (mark >= 90 and mark <= 100):
    print("Excellent")
elif ( mark < 90 and mark >=75 ):
    print("Good")
elif ( mark < 75 and mark >=50 ):
    print("Pass")
else:
    print("Fail")

    
