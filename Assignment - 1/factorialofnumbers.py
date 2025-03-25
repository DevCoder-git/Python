#write a python program to find the factorial of a number

#algorithm
#1. Start
#2. Read the number
#3. Initialize fact=1
#4. Repeat the steps 5 and 6 until i becomes n
#5. Multiply fact by i
#6. Increment i by 1
#7. Print the factorial
#8. Stop

a=int(input("Enter a number : "))
fact=1
for i in a:
    fact*=i
print("The factorial of the given number is : ",fact)

#result

#Enter a number : 5
#The factorial of the given number is : 120
