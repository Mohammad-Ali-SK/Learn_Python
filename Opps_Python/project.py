class Student:
    def __init__(self,name, roll , class_no):
        self.name = name
        self.roll = roll
        self.class_no = class_no
        self.marks = {}
    def add_marks(self,subject,marks):
        if subject in self.marks:
            print(f'{marks} is already has {subject}')
        else:
            self.marks[subject] = marks
    def calculate_avg(self):
        if not self.marks:
            print("There are no marks are here")
        total_marks = sum(self.marks.values())
        avg_marks = total_marks/len(self.marks)
        return avg_marks
    def show_details(self):
        print(f'Student Information')
        print(f'Student name is {self.name}')
        print(f'Student roll is {self.roll}')
        print(f'Class : {self.class_no}')
        print(f'Avg marks is {self.calculate_avg()}')

student1 = Student('ALi', 78, '12th')
student1.add_marks('Math', 79)

student1.show_details()