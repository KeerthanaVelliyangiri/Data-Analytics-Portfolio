class student:
    def __init__(self,name,id,dept,mark):
        self.name=name
        self.id=id
        self.dept=dept
        self.mark=mark
        self.attendance=0
    def display(self):
        return f"Name:{self.name} \n ID:{self.id} \n Dept:{self.dept} \n Mark:{self.mark} \n Attendence:{self.attendance}"
    def avg(self):
        self.avg = sum(self.mark)//len(self.mark)
        return self.avg
    
stds=[]
n=0
while n<3:
    stds.append("")
    name=input("Enter student name :")
    id=input("Enter student id :")
    dept=input("Enter dept :")
    marks=[]
    for i in range(3):
        mark=int(input("enter marks : "))
        marks.append(mark)
    stds[n]=student(name,id,dept,marks)
    n+=1

print(stds[1].display())
print(stds[1].avg())



