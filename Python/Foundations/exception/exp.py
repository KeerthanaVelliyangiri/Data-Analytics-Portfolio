# age=int(input("enter age : "))
# print(age)

# int - 55
# string - ValueError: invalid literal for int() with base 10: 'twenty'

# using try catch

# try:
#    age=int(input("enter age : "))
#    print(age)
# except ValueError :
#    print("plx enter valid input") 


# FileNotFoundError

# file=open("datas.txt","r")
# print(file.read())

#

# try:
#     files=open("datas.txt", "r")
#     print(files.read())   
# except PermissionError:
#     print("Permission denied:")

# using try,except,else-success

# try:
#    age=int(input("enter age : "))
#    print(age)
# except:
#    print("plx enter valid input") 
# else:
#     print("valid input")  

# using try,except,else,finally-success/failure

# try:
#    age=int(input("enter age : "))
#    print(age)
# except:
#    print("plx enter valid input") 
# else:
#     print("valid input") 
# finally:
#    print("successfully") 

# PermissionError

# set the permission - icacls "C:\Users\91636\OneDrive\Desktop\Data-Analytics-Portfolio\Python\Foundations\exception\data.txt" /deny "$env:USERNAME`:R"

# with open(r"C:\Users\91636\OneDrive\Desktop\Data-Analytics-Portfolio\Python\Foundations\exception\data.txt", "r") as file:
#     print(file.read())
#     file.write()   
#     # or
#     # print(data)



