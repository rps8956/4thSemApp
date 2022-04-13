class player1:

    def __init__(self,runs):
        self.runs = runs

    def total(self):
        tot_runs = 0
        for el in range(0,len(runs)):
            tot_runs = tot_runs+runs[el]
        print("total runs 1",tot_runs)

class player2:

    def __init__(self,runs2):
        self.runs2 = runs2

    def total(self):
        tot_runs2 = 0
        for el in range(0,len(runs2)):
            tot_runs2 = tot_runs2+runs2[el]
        print("Total runs 2:",tot_runs2)

runs = []
obj = player1(runs)
run = 2
while (run != 0):
            #print("Enter your runs in 2,4,6,8: ")
            run = int(input("friend1: "))
            if (run == 2):
                runs.append(2)
            elif (run == 4):
                runs.append(4)
            elif (run == 6):
                runs.append(6)
            elif (run == 8):
                runs.append(1)
            elif (run == 0):
                print("OUT")
                break
            else:
                print("Invalid run")

runs2 = []
obj2 = player2(runs2)
run = 2
while (run != 0):
            #print("Enter your runs in 2,4,6,8: ")
            run = int(input("friend2: "))
            if (run == 2):
                runs2.append(2)
            elif (run == 4):
                runs2.append(4)
            elif (run == 6):
                runs2.append(6)
            elif (run == 8):
                runs2.append(1)
            elif (run == 0):
                print("OUT")
                break
            else:
                print("Invalid run")

y = player1(runs)
y.total()
x = player2(runs)
x.total()
if (runs>runs2):
    print("Winner:friend1")
elif (runs<runs2):
    print("Winner:friend2")
else:
    print("Match has been tied")