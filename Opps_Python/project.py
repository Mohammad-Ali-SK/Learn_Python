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
# class Factory:
#     def __init__(self,BT,ET,TY):
#         self.BT = BT
#         self.ET = ET
#         self.TY = TY

# ferari = Factory('Covered','8 Cycle', 8)

# print(ferari.TY)

# class Fac:
#     def __init__(self,bt,et,ty):
#         self.bt = bt
#         self.et = et
#         self.ty = ty
#     def showDetails(self):
#         print(f'Your details are  {self.bt} , {self.et}, {self.ty}')
        
# class Fac2(Fac):
#     def __init__(self, bt, et, ty,glass):
#         super().__init__(bt, et, ty)
#         self.glass = glass
#     def showDetails(self):
#         print(f'Your details are  {self.bt} , {self.et}, {self.ty} , {self.glass}')


# ferari = Fac('Covered','8 cycle', 4)
# alto = Fac2('Covered','8 cycle', 4, 'Iron')
# ferari.showDetails()
# alto.showDetails()

class Student:
    def __init__(self,name,class_name,roll_num):
        self.name = name
        self.class_name = class_name
        self.roll_num = roll_num
        self.marks = {}
    def add_marks(self,subject,marks):
        if subject in self.marks:
            print(f'This subject is already exit')
        else:
            self.marks[subject] = marks
    
    def calculation_avg(self):
        if not self.marks:
            print('There are no subject are here')
        total = sum(self.marks.values())
        avg_marks = total/len(self.marks)
        return avg_marks
    
    def show_detail(self):
        print('Student Details is__')
        print(f'roll_{self.roll_num} name_{self.name}  class_{self.class_name} marks = {self.marks}  Avarage marks is _{self.calculation_avg()}')

student1 = Student('ALi',8,78)
student1.add_marks('Math',89)
student1.show_detail()