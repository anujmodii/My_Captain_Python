a=[]
for i in range(5):
    n=int(input("Enter a value"))
    a.append(n)

fn=lambda x,y:x*y
from functools import reduce
result=reduce(fn,a)
print(result)
