set1 = set()
set2 = set()
var1 = str(input())
var2 = str(input())
splitvar1 = var1.split(",")
splitvar2 = var2.split(",")
t1 = set()
t2 = set()
for i in splitvar1:
    t1.add(i)

for i in splitvar2:
    t2.add(i)

operation = int(input("Choose one operation 1)Add 2)Remove 3)difference 4)intersection"))

global ch_set
ch_set = int(input("Choose one set"))
def add(ch_set):
    addition = str(input("Enter element to add"))
    if ch_set ==1:
        t1.add(addition)
        print(sorted(t1))
    elif ch_set == 2:
        t2.add(addition)
        print(sorted(t2))
def sub(ch_set):
    subtraction = str(input("Enter element to subtract"))
    if ch_set == 1:
        t1.remove(subtraction)
        print(sorted(t1))
    elif ch_set == 2:
        t2.remove(subtraction)
        print(sorted(t2))
def diff():
    difference = t1 - t2
    print(difference)
def inter():
    intersection = t1 & t2
    print(intersection)
if operation == 1:
    add(ch_set)
if operation == 2:
    sub(ch_set)
if operation == 3:
    diff()
if operation == 4:
    inter()



