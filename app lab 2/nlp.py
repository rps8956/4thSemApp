gazettear = {1:'Apple', 2:'Oracle',3:'Advanced Programming Practice',4:'Software Project Management', 5:'Fundamentals of mathematics'}

def nlp(dict):
    char = 0
    for x in gazettear.values():
        for element in x:
            space = x.count(" ")
            char = char+1
        res = char-space
        print(x,":",res)
        char = 0


nlp(gazettear)

