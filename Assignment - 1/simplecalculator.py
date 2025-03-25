#simple calculator
a=int(input("Enter first number : "))
b=int(input("Enter second number : "))
c=input("Enter the operator : ")
if(c=='+'):
    print("The sum of 2 numbers is : ",a+b)
elif(c=='-'):
    print("The difference of 2 numbers is : ",a-b)
elif(c=='*'):
    print("The product of 2 numbers is : ",a*b)
elif(c=='/'):
    print("The division of 2 numbers is : ",a/b)
else:
    print("Invalid operator")
