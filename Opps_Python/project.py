# class Student:
#     def __init__(self,name, roll , class_no):
#         self.name = name
#         self.roll = roll
#         self.class_no = class_no
#         self.marks = {}
#     def add_marks(self,subject,marks):
#         if subject in self.marks:
#             print(f'{marks} is already has {subject}')
#         else:
#             self.marks[subject] = marks
#     def calculate_avg(self):
#         if not self.marks:
#             print("There are no marks are here")
#         total_marks = sum(self.marks.values())
#         avg_marks = total_marks/len(self.marks)
#         return avg_marks
#     def show_details(self):
#         print(f'Student Information')
#         print(f'Student name is {self.name}')
#         print(f'Student roll is {self.roll}')
#         print(f'Class : {self.class_no}')
#         print(f'Avg marks is {self.calculate_avg()}')

# student1 = Student('ALi', 78, '12th')
# student1.add_marks('Math', 79)

# student1.show_details()



class Student:
    def __init__(self,name,roll,class_no):
        self.name = name
        self.roll = roll
        self.class_no = class_no
        self.marks = {}
    def add_marks(self,subject,marks):
        if subject in self.marks:
            print("This this is already declear")
        else:
            self.marks[subject] = marks
    def cal_avg(self):
        if not self.marks:
            print("No Marks is here ")
        total = sum(self.marks.values())
        avg = total/len(self.marks)
        return avg
    def student_details(self):
        print(f'Student Information')
        print(f'Student name is {self.name} and Roll No _{self.roll} Class --{self.class_no}')
        print(f'{self.marks}')
        print(f'Avarage Marks is {self.cal_avg()}')

student1 = Student('Rohit',78,'8th')
student1.add_marks('Math',89)
student1.add_marks('English',67)
student1.add_marks('Science',80)
student1.add_marks('History',56)
 
student1.student_details()