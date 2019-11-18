a=[]
for i in range(10):
    n=int(input("Enter a value"))
    a.append(n)
odd=0
even=0
for i in a:
    if i%2!=0:
        odd+=1
    else:
        even+=1
print("No. of odd terms = %s\nNo. of even terms=%s" %(odd,even))
