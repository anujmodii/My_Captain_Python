l=[]
for i in range(5):
    a=input("Enter a word for the list")
    l.append(a)
for i in range(5):
    l[i]=len(l[i])
print(max(l))
