from abc import ABC,abstractmethod

class person(ABC):
    def __init__(self,name,email):
        self.name=name
        self.email=email
    @abstractmethod
    def display_role(self):
        return "university person"
    @abstractmethod
    def display_dashboard(self):
        pass
    
class student(person):
    def __init__(self,name,email,dept):
        super().__init__(name,email)
        self.dept=dept

    def display_role(self):
            return "student"
    def display_dashboard(self):
            return "student dashboard"
    
class teacher(student):
    def __init__(self,name,email,dept,sub):
        super().__init__(name,email,dept)
        self.sub=sub
    def display_role(self):
            return "teacher"
    def display_dashboard(self):
            return "teacher dashboard"


std1=student("keerthi","keerthi@gmail.com","cse")
print(std1.display_role())

people=[
     student("vasu","vasu@gmail.com","it"),
     teacher("riti","rit@gmail.com","it",["cs","ai"])
]

for person in people:
     print(person.display_role())



