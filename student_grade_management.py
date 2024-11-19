class marks:
    def __init__(self,subject,total):
        self.subject = subject
        self.score = 0
        self.no_subjects = 0
        self.fail = False
        self.total = total
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

class Student(marks):
    def __init__(self,id,subject="",name = "",total = 0):
        super().__init__(subject,total)
        self.name = name
        self.id = id
    def input_name(self):
        self.name = input("Enter the name :")
    def display(self):
        print("\n-----STUDENT'S REPORT-----")
        print(f"Name : {self.name}")
        print(f"ID : {self.id}")
        print(f"Score : {self.subject_dict}")
        print(f"Total Score : {self.total}")
        print(f"Average : {self.average}")
        print(f"Status : {self.performance}")
        print("--------------------------")
    def grade_card(self):
        filename = f"GradeCard_{self.id}.txt"
        with open(filename,"w") as file:
            file.write("-----STUDENT'S REPORT-----\n")
            file.write(f"Name : {self.name}\n")
            file.write(f"ID : {self.id}\n")
            file.write(f"Score : {self.subject_dict}\n")
            file.write(f"Total Score : {self.total}\n")
            file.write(f"Average : {self.average}\n")
            file.write(f"Status : {self.performance}\n")
            file.write("--------------------------\n")

class_marks = []
student_list = []  

def create_student(no_of_students):
    for j in range(0,no_of_students):
        roll_no = int(input("Enter the student id : "))
        obj_name = Student(roll_no)
        student_list.append(obj_name)
    for student in student_list:
        student.input_name()
        student.input_marks_subject()
        student.total_average()
        student.status()
    for student in student_list:
        class_marks.append(student.total)
    for student in student_list:
        student.display()
    for student in student_list:
        student.grade_card()
    print(f"\nHighest marks in the class : {max(class_marks)}")
    print(f"Lowest marks in the class : {min(class_marks)}")

no_of_students = int(input("Enter the number of students : "))
create_student(no_of_students)

