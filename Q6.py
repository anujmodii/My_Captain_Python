a=int(input("Enter 1st side"))
b=int(input("Enter 2nd side"))
c=int(input("Enter 3rd side"))
if a==b and b==c:
            print("Equilateral Triangle")
elif a!=b and b!=c and a!=c:
     print("Scalene Triangle")
else:
     print("Isosceles Triangle")
