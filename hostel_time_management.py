class study_time:
    def __init__(self,morning,noon,evening,target):
        self.morning = morning
        self.noon = noon
        self.evening = evening
        self.target = target
        self.success = False
        self.total  = 0
    def total_time(self):
        self.total = self.morning + self.noon + self.evening
    def daily_target(self):
        self.success = (self.target <= self.total)
    def display(self):
        if 0 <= self.total <= 24:
            print("Total study hours = ",self.total)
        else:
            print("Error")

        if self.success:
            print("You met your target")
        else:
            print("Target not met")

todays_target = int(input("Enter today's target : "))
morning_time = int(input("Enter morning hours : "))
noon_time = int(input("Enter afternoon hours : "))
eve_time = int(input("Enter evening hours : "))

day1 = study_time(morning_time,noon_time,eve_time,todays_target)
day1.total_time()
day1.daily_target()
day1.display()