class ebill:
    def __init__(self,p_read,c_read):
        self.p_read = p_read
        self.c_read = c_read

    def cal(self):
        to_pay = 0
        actual_read = (self.c_read - self.p_read)
        if (0<=actual_read<=100):
            to_pay = 0
        elif (100<actual_read<=200):
            to_pay = (actual_read-100)*1
        elif (200<actual_read<=300):
            to_pay = (100*0)+(100*1)+(actual_read-200)*2
        elif(actual_read>300):
            to_pay = (100*0)+(100*1)+(100)*2+(actual_read-300)*3
        print("Bill amount:",to_pay)

p_read = int(input("Previous Reading:"))
c_read = int(input("Current Reading:"))
b1 = ebill(p_read,c_read,)
b1.cal()
