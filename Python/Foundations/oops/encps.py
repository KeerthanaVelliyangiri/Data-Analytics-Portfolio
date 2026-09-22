# class student:
    
#     def __init__(self,attendance):

#     # protect
#         self._attendance=attendance 
#         if 0 <= attendance <= 100:
#             self._attendance=attendance
#         else:
#             raise ValueError("Please enter valid number") 

#     # protect the date - when we see the date protect date using getter
#     def get_attendance(self):
#         return self._attendance

#     # set the limit use setter
#     def set_attendance(self,value):
#         if 0 <= value <= 100:
#             return value
#         else:
#             # raise ValueError("Please enter valid number")
#             return "Please enter valid number"


# std1=student(90)

# print(std1.get_attendance())

# std2=student(900)

# print(std1.get_attendance())

class student:
    
    def __init__(self,name,id,dept,mark,attendance):
        self.name=name
        self.id=id
        self.dept=dept
    # protect mark
        for m in mark:
            if not (0 <= m <= 100):
                raise ValueError("Marks must be between 0 and 100")
        self._mark=mark

    # protect attendance 
        self._attendance=attendance 
        if 0 <= attendance <= 100:
            self._attendance=attendance
        else:
            raise ValueError("Please enter valid number") 

    # display student info (marks hidden, only CGPA shown)
    def display(self):
        return f"Name: {self.name}\n ID: {self.id} \n Department: {self.dept} \n Attendance: {self._attendance} \n CGPA: {self.cgpa()}"

    # protect the date - when we see the date protect date using getter
    def get_attendance(self):
        return self._attendance

    # set the limit use setter
    def set_attendance(self,value):
        if 0 <= value <= 100:
            return value
        else:
            return "Please enter valid number"

    # calculate CGPA
    def cgpa(self):
        avg = sum(self._mark) / len(self._mark)
        self.cgpa = round(avg / 10, 2)
        return self.cgpa

    # set the marks use setter
    def set_marks(self, new_marks):
        for m in new_marks:
            if not (0 <= m <= 100):
                return "Enter marks between 0 to 100"
        self._marks = new_marks


# Example
std1 = student("keerthi", "CS501", "cse", [85, 90, 89], 89)
std2 = student("dhana", "IT601", "it", [75, 89, 80], 90)

print(std1.display())
print(std2.display())



