from functools import reduce

nums = [0,4,2,6,4,8,9,1]
evens = list(filter(lambda n:n%2==0,nums))#filter
print(evens)

doubles = list(map(lambda n:n*2,evens))#map
print(doubles)

sum = reduce(lambda a,b:a+b,doubles)# reduce
print(sum)