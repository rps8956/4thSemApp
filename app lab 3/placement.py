class placement:

    def __init__(self,name,cgpa,gender,backlogs):
        self.name = name
        self.cgpa = cgpa
        self.gender = gender
        self.backlogs = backlogs
    def check(self):
        if self.cgpa>7.0 and self.backlogs == 0:
            print("Yes,you are eligible")
        else:
            print("No,you are not eligible")
name = str(input("Enter your name"))
cgpa = float(input("Enter your cgpa"))
gender = str(input("Enter your gender"))
backlogs = int(input("Enter the number of backlogs"))
s1 = placement(name,cgpa,gender,backlogs)
s1.check()
