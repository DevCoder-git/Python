#write a program to check whether a string is palindrome or not
#algorithm
#1. Start
#2. Read the string
#3. Reverse the string
#4. Compare the string with the reversed string
#5. If they are equal, print "Palindrome"
#6. Else, print "Not Palindrome"
#7. Stop

a=str(input("Enter a string"))
b=a[::-1]
if(a==b):
    print("Palindrome")
else:
    print("Not Palindrome")

#result
#Enter a string : malayalam
#Palindrome

