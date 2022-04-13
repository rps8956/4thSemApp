t1 = (1, 2, 3, 4)
t2 = (3, 5, 2, 1)
t3 = (2, 2, 3, 1)

def encoder(t1,t2,t3):
  av1 = (t1[0]+t2[0]+t3[0])/3
  avg2 = (t1[1]+t2[1]+t3[1])/3
  avg3 = (t1[2]+t2[2]+t3[2])/3
  avg4 = (t1[3]+t2[3]+t3[3])/3

  t4 = (av1,avg2,avg3)
  print(t4)

encoder(t1,t2,t3)

