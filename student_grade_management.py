class marks:
    def __init__(self,subject):
        self.subject = subject
        self.score = 0
        self.no_subjects = 0
        self.fail = False
    def input_marks_subject(self):
        self.no_subjects = int(input("Enter no. of subjects :"))
        self.subject_dict = dict()
        for i in range(0,self.no_subjects):
            self.subject = input("Enter the subject :")
            self.score = int(input("Enter the marks :"))
            self.subject_dict[self.subject] = self.score
    def total_average(self):
        self.total = sum(self.subject_dict.values())
        self.average = self.total/self.no_subjects
    def status(self):
        if self.average <= 16:
            self.fail = True
        self.performance = "FAIL" if self.fail else "PASS"

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
        print(f"Marks : {self.subject_dict}")
        print(f"Total marks : {self.total}")
        print(f"Average : {self.average}")
        print(f"Status : {self.performance}")
    
student1 = student(2411981626)
student1.input_name()
student1.input_marks_subject()
student1.total_average()
student1.status()
student1.display()