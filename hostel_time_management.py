class study_time:
    def __init__(self,morning,noon,evening):
        self.morning = morning
        self.noon = noon
        self.evening = evening
    def total_time(self):
        self.total = self.morning + self.noon + self.evening
    def display(self):
        print("Total study hours = ",self.total)

day1 = study_time(4,3,5)
day1.total_time()
day1.display()