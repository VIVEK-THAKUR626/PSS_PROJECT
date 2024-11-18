class marks:
    def __init__(self,subject,score = 0):
        self.subject = subject
        self.score = score
    def input_marks_subject(self):
        self.subject = input("Enter the subject :")
        self.score = int(input("Enter the marks :"))
    
class student(marks):
    def __init__(self,id,subject="",name = ""):
        super().__init__(subject)
        self.name = name
        self.id = id
    def input_name(self):
        self.name = input("Enter the name :")
    def display(self):
        print()
        print(f"Student name : {self.name}")
        print(f"Student ID : {self.id}")
        print(f"Subject : {self.subject}")
        print(f"Marks : {self.score}")
    
student1 = student(2411981626)
student1.input_name()
student1.input_marks_subject()
student1.display()