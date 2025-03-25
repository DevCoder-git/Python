#write a python program to find the sum of all even numbers from 0 to n
#algorithm
#1. Start
#2. Read the value of n
#3. Initialize sum=0
#4. Repeat the steps 5 and 6 until i becomes n
#5. If i is even, add i to sum
#6. Increment i by 1
#7. Print the sum

n=int(input("Enter the value of n : "))
sum=0
for i in range(0,n+1):
    if(i%2==0):
        sum=sum+i
print("The sum of all even numbers from 0 to",n,"is",sum)

#result
#Enter the value of n : 10
#The sum of all even numbers from 0 to 10 is 30
