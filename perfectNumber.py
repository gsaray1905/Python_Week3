from functools import reduce
perfectNumberList=[]

def perfectNumber(x):
    total = 0
    for num in range(1,x):
        if x % num == 0:
            total += num
    return total == x

for x in range(2,1000):
    if perfectNumber(x):
        perfectNumberList.append(x)
print("The perfect numbers between 1 an 1000 are",perfectNumberList)
filter(lambda z: z<1000, perfectNumberList)
result = (reduce(lambda a,b: a + b, perfectNumberList))
print("Sum of the perfect numbers:", result)