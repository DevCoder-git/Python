#write a python program to find the roots of a quadratic equation

#algorithm
#1. Start
#2. Read the values of a,b and c
#3. Calculate the roots of the quadratic equation
#4. Print the roots of the quadratic equation
#5. Stop


a=int(input("Enter the value of a : "))
b=int(input("Enter the value of b : "))
c=int(input("Enter the value of c : "))
d=(-b+((b**2)-(4*a*c))**0.5)/(2*a)
e=(-b-((b**2)-(4*a*c))**0.5)/(2*a)
print("The roots of the quadratic equation are : ",d,e)

#result
#Enter the value of a : 1
#Enter the value of b : 5
#Enter the value of c : 6
#The roots of the quadratic equation are :  -2.0 -3.0
#the expected output has been obtained successfully
