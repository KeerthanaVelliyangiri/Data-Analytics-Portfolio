# ct=3
# while ct>=0:
#     std=input("Enter  name")
#     ct-=1
file=open(r"C:\Users\91636\OneDrive\Desktop\Data-Analytics-Portfolio\Python\Foundations\oops\filehandle\stddetail.txt","r")
print(file.read())

# with open(r"C:\Users\91636\OneDrive\Desktop\Data-Analytics-Portfolio\Python\Foundations\oops\filehandle\stddetail.txt","r")as file:
#     content=file.read()
#     print(file.read())

with open(r"C:\Users\91636\OneDrive\Desktop\Data-Analytics-Portfolio\Python\Foundations\oops\filehandle\stddetail.txt","r+")as file:
    file.write("pavi")
    content=file.read()
    print(content)