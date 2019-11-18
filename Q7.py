a=[]
for i in range(3):
    n=int(input("Enter a value"))
    a.append(n)
max=a[0]
for i in a:
   if i<max:
       max=i
med=a[0]
for i in a:
    if i<max and i!=max :
        med=i
print("Median=",med)
