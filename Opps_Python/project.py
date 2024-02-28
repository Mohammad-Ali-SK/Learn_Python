class Student:
    def __init__(self,name,roll_number, class_name):
        self.name = name
        self.roll_number = roll_number
        self.class_name = class_name
        self.marks = {}
        
    def add_marks(self,subject,marks):
        if subject in self.marks:
            print(f'{self.marks} is already marks of {subject}')
        else:
            self.marks[subject] = marks
    
    def calculate_avg(self):
        if not self.marks:
            print(f'There are no avb marks')
        total_marks = sum(self.marks.values())
        avg_marks = total_marks/len(self.marks)
        return avg_marks
    
    def show_details(self):
        print(f'Student Information')
        print(f'Name : {self.name}')
        print(f'Roll No : {self.roll_number}')
        print(f'Class : {self.class_name}')
        print(f'Avg marks is {self.calculate_avg()}')

student1 = Student('ALi',12, '12th')
student2 = Student('Amir', 23, '8th')

student1.add_marks('English', 67)
student1.add_marks('Math', 89)

student2.add_marks('Science', 56)
student2.add_marks('History', 78)

student1.show_details()
student2.show_details()

