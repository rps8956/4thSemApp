class player1:

    def __init__(self,runs):
        self.runs = runs
    def total(self):
        tot_runs = 0
        for el in range(0,len(runs)):
            tot_runs = tot_runs+runs[el]
        print(tot_runs)
runs  = []
obj = player1(runs)
run = 2
while(run!=0):
    print("Enter your runs in 2,4,6,8: ")
    run = int(input("Enter your run: "))
    if (run==2):
        runs.append(2)
    elif(run==4):
        runs.append(4)
    elif(run==6):
        runs.append(6)
    elif(run==8):
        runs.append(1)
    elif(run==0):
        print("OUT")
        break
    else:
        print("Invalid run")

class player2:
    def __init__(self,runs2):
        self.runs2 = runs2
    def total(self):
        tot_runs = 0
        for el in range(0,len(runs2)):
            tot_runs = tot_runs+runs[el]
        print(tot_runs)

runs2  = []
obj2 = player2(runs2)
run2 = 2
while(run2!=0):
    print("Enter your runs in 2,4,6,8: ")
    run = int(input("Enter your run: "))
    if (run2==2):
        runs2.append(2)
    elif(run2==4):
        runs2.append(4)
    elif(run2==6):
        runs2.append(6)
    elif(run2==8):
        runs2.append(1)
    elif(run2==0):
        runs2.append(0)
        print("OUT")
        break


    else:
        print("Invalid run")

y = player1(runs)
y.total()
x = player2(runs2)
x.total()
