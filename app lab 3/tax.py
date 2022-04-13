class aadhar:
    def __init__(self,name,age,gender,address):
        self.name = name
        self.age = age
        self.gender = gender
        self.address = address
    def enter1(self):
        self.name = str(input("enter your name"))
        self.age = int(input("enter your age"))
        self.gender = str(input("Enter your gender"))

class pan(aadhar):
    def __init__(self,b_ac,name,age,gender,address):
        aadhar.__init__(name,age,gender,address)
        self.b_ac = b_ac

    def enter2(self):
        self.b_ac = input("Enter bank account no.")

class faculty(aadhar):
    def __init__(self,f_id,name,age,gender,address):
        aadhar.__init__(self,name, age, gender, address)
        self.f_id = f_id

    def enter3(self):
        self.f_id = input("Enter your faculty id:")

class IT_card(aadhar,pan,faculty):
    def __init__(self,name,age,gender,address):
        aadhar.__init__(self, name, age, gender, address)
        pan.__init__(self,self.b_ac)
        faculty.__init__(self,self.f_id)
    def display(self):
        print("name:",self.name)
        print("age:",self.age)

x = IT_card()
x.display()
