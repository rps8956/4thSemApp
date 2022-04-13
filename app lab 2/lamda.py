t = (3,-5,7,-9,1,4,-6)

p_sum = tuple(filter(lambda nums:nums<0,t))
n_sum = tuple(filter(lambda nums:nums>0,t))

print("Sum of the positive numbers: ",sum(p_sum))
print("Sum of the negative numbers: ",sum(n_sum))