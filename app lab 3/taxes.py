

class aadhar():
    def __init__(self,address):
        #IT_card.__init__(name,dob,gender)
        self.address = address
    def display(self):
        print("Address:{}".format(self.address))

class pan():
    def __init__(self,b_ac):
        #IT_card.__init__(name,dob,gender)
        self.b_ac = b_ac
    def display(self):
        print("bank acount no.:{}".format(self.b_ac))

class faculty():
    def __init__(self,f_id):
        #IT_card.__init__(name,dob,gender)
        self.f_id = f_id
    def display(self):
        print("Faculty ID:{}".format(self.f_id))

class IT_card(aadhar,pan,faculty):

    def __init__(self,name,dob,gender,address,b_ac,f_id):
       # super().__init__(address,b_ac,f_id)
        aadhar.__init__(self,address)
        pan.__init__(self,b_ac)
        faculty.__init__(self,f_id)

        self.name = name
        self.dob = dob
        self.gender = gender
    def display(self):
        print("Name:{}\nDate of Birth:{}\nGender:{}\nAddress:{}\nBank Account:{}\nFaculty ID:{}".format(self.name,self.dob,self.gender,self.address,self.b_ac,self.f_id))


name = str(input("Enter your name:"))
dob = int(input("Enter your date of birth:"))
gender = str(input("Enter your gender:"))
address = input("Enter your address:")
b_ac = input("Enter your Bank Account number:")
f_id = input("Enter your faculty ID:")

x = IT_card(name,dob,gender,address,b_ac,f_id)
x.display()